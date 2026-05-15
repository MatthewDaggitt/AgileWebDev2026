from app.controllers import create_new_group
from app.models import Group

from flask import render_template, request, redirect, url_for

from app import db
from app.blueprints import main

@main.route('/deleteGroup/<int:group_id>', methods=['POST'])
def delete_group(group_id):
    if group_id:
        db.session.query(Group).filter(Group.group_id == group_id).delete()
        db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/newGroup', methods=['POST'])
def new_group():
    groups = db.session.query(Group).all()

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

    try:
        create_new_group(groups, group_members, student1, student2, student3, student4)
    except ValueError as e:
        error_message = str(e)
        return render_template('index.html', all_groups=groups, error_message=error_message)

    return redirect(url_for('main.index'))
    
@main.route('/', methods=['GET'])
def index():
    groups = db.session.query(Group).all()
    return render_template('index.html', all_groups=groups)

@main.route('/page')
def bootstrap():
    return render_template('bootstrap.html')