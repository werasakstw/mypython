from flask import Flask
app = Flask(__name__)

from student_view import student
app.register_blueprint(student)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
