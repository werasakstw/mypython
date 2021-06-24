from flask import Blueprint
student = Blueprint('student', __name__)

@student.route('/student/hello/<name>')
def student_hello(name):
    return 'Hello ' + name + ' I am student_hello.'
# curl 127.0.0.1:8080/student/hello/John

from models import Student
@student.route('/student/john')
def john():
    return str(Student('john', 'cs', 1.8))
# curl 127.0.0.1:8080/student/john
