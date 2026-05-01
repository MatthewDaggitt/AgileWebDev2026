
from dataclasses import dataclass
from typing import Optional
from app import db

class Group(db.Model):
    group_id = db.Column(db.Integer, primary_key=True)
    student1 = db.Column(db.String(8), nullable=False)
    student2 = db.Column(db.String(8), nullable=False)
    student3 = db.Column(db.String(8), nullable=False)
    student4 = db.Column(db.String(8), nullable=True)


def create_test_data():
    group1 = Group(
        group_id=1,
        student1="00123456",
        student2="00123452",
        student3="00123453",
        student4="00123451",
    )

    group2 = Group(
        group_id=2,
        student1="20123456",
        student2="20123452",
        student3="20123453",
        student4="20123451",
    )

    group3 = Group(
        group_id=3,
        student1="02123456",
        student2="04123452",
        student3="03123453",
        student4="01123451",
    )
            

    groups = [group1, group2] # group3]

    db.session.add_all(groups)
    db.session.commit()