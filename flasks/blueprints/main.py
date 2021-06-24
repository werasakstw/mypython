
from flask import Flask
app = Flask(__name__)

from root_view import root
app.register_blueprint(root)

from student_view import student
app.register_blueprint(student)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
