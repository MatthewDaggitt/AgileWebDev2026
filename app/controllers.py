from typing import Optional

from app import db
from app.models import Group


def create_new_group(
        groups: list[Group],
        group_members:int,
        student1: Optional[str],
        student2: Optional[str],
        student3: Optional[str],
        student4: Optional[str]
    ) -> Group:
    
    is_valid_member_count = 1 <= group_members <= 4
    if not is_valid_member_count:
        raise ValueError('Group size must be between 1 and 4 members.')

    check_valid_student(group_members, 1, student1)
    check_valid_student(group_members, 2, student2)
    check_valid_student(group_members, 3, student3)
    check_valid_student(group_members, 4, student4)

    submitted_students = [student1, student2, student3, student4]
    required_students = submitted_students[:group_members]

    has_all_required_students = all(required_students)
    has_duplicates = len(required_students) != len(set(required_students))

    if (
        is_valid_member_count
        and has_all_required_students
        and not has_duplicates
    ):
        next_group_id = (max(group.group_id for group in groups) + 1) if groups else 1

        new_group = Group(
            group_id=next_group_id,
            student1=required_students[0] if group_members >= 1 else '',
            student2=required_students[1] if group_members >= 2 else '',
            student3=required_students[2] if group_members >= 3 else '',
            student4=required_students[3] if group_members >= 4 else None,
        )
        db.session.add(new_group)
        db.session.commit()
        return new_group
    
def check_valid_student(expected_number, student_number, student_id: Optional[str]):
    # print(expected_number, student_number, student_id, student_id is not None or student_id != '')
    if student_number > expected_number:
    #     if student_id is not None or student_id != '':
    #         raise ValueError(f"Student {student_number} should not be provided for a group of {expected_number} members.")
        return
    
    if not student_id:
        raise ValueError(f"Student {student_number} is required.")
    
    if not student_id.isdigit() or len(student_id) != 8:
        raise ValueError(f"Student {student_number} ID must be an 8-digit number.")