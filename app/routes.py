from app.models import Group, groups

from flask import render_template, request, redirect, url_for

from app import app

@app.route('/deleteGroup/<int:group_id>', methods=['POST'])
def delete_group(group_id):
    if group_id:
        global groups
        groups = [group for group in groups if group.group_id != group_id]
    return redirect(url_for('index'))

@app.route('/newGroup', methods=['POST'])
def new_group():
    error_message = None
    try:
        group_members = int(request.form.get('grpMembers', '').strip())
    except (TypeError, ValueError):
        error_message = 'Please enter a valid number of group members (1 to 4).'
        return render_template('index.html', all_groups=groups, error_message=error_message)

    student1 = request.form.get('Std1', '').strip()
    student2 = request.form.get('Std2', '').strip()
    student3 = request.form.get('Std3', '').strip()
    student4 = request.form.get('Std4', '').strip()

    is_valid_member_count = 1 <= group_members <= 4
    if not is_valid_member_count:
        error_message = 'Group size must be between 1 and 4 members.'
        return render_template('index.html', all_groups=groups, error_message=error_message)

    submitted_students = [student1, student2, student3, student4]
    required_students = submitted_students[:group_members]

    has_all_required_students = all(required_students)
    has_numeric_ids = all(student.isdigit() for student in required_students)
    has_duplicates = len(required_students) != len(set(required_students))

    if (
        is_valid_member_count
        and has_all_required_students
        and has_numeric_ids
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
        groups.append(new_group)
        return redirect(url_for('index'))
    
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', all_groups=groups)

@app.route('/page')
def bootstrap():
    return render_template('bootstrap.html')