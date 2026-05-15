
from unittest import TestCase

from app import create_app, db
from app.config import TestConfig
from app.controllers import create_new_group
from app.models import Group, Student, create_test_data

class BasicTests(TestCase):
    def setUp(self):
        testApp =  create_app(TestConfig)
        self.app_context = testApp.app_context()
        self.app_context.push()
        db.create_all()
        create_test_data()
        return super().setUp()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        return super().tearDown()
    
    def test_group_creation(self):
        group = create_new_group(
            groups=Group.query.all(),
            group_members=3,
            student1="12345678",
            student2="87654321",
            student3="11223344",
            student4=None
        )

        retrieved_group = Group.query.filter_by(group_id=group.group_id).first()
        self.assertIsNotNone(retrieved_group)

    def test_group_creation_with_invalid_group_size(self):
        with self.assertRaises(ValueError, msg="Group size must be between 1 and 4 members."):
            create_new_group(
                groups=Group.query.all(),
                group_members=5,
                student1="12345678",
                student2="87654321",
                student3="11223344",
                student4="44332211"
            )
    