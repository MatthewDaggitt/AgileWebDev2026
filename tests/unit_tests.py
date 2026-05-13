
from unittest import TestCase

from app import create_app, db
from app.config import TestConfig
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
    
    def test_password_hashing(self):
        pass