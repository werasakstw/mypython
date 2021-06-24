from flask import render_template, request, redirect, url_for
from myutil import send_get, send_post, send_put, send_delete

from flask import Blueprint
student = Blueprint('student', __name__)

@student.route("/student/init")
def init():
    send_get('http://127.0.0.1:8081/student/init')
    return 'Create and init students table.'

import json
@student.route('/student/list')
def list():
    students = json.loads(send_get('http://127.0.0.1:8081/student/list'))
    return render_template('list.html', students=students)

@student.route('/student/new', methods=["POST"])
def new():
    return render_template('new.html')

@student.route('/student/save', methods=["POST"])
def save():
    name = request.form['name']
    dep = request.form['dep']
    gpa = float(request.form['gpa'])
    send_put('http://127.0.0.1:8081/student/save', \
		data={'name': name, 'dep': dep, 'gpa': gpa })
    return redirect(url_for('student.list'))

@student.route('/student/edit/<int:sid>')
def edit(sid):
    s = json.loads(send_get('http://127.0.0.1:8081/student/get/'+ str(sid)))
    return render_template('edit.html', student=s)

@student.route('/student/update/<int:sid>',  methods=["POST"])
def update_(sid):
    if request.form['_method'] == 'PUT':
        name = request.form['name']
        dep = request.form['dep']
        gpa = float(request.form['gpa'])
        send_post('http://127.0.0.1:8081/student/update/' + str(sid), \
	 data={'name': name, 'dep': dep, 'gpa': gpa})
    return redirect(url_for('student.list'))

@student.route('/student/delete/<int:sid>',  methods=["POST"])
def delete(sid):
    if request.form['_method'] == 'DELETE':
        send_delete('http://127.0.0.1:8081/student/delete/' + str(sid))
    return redirect(url_for('student.list'))


