from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db = SQLAlchemy(app)
admin = Admin(app, name='Models', template_mode='bootstrap3')

# Models
class Student(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    dep = db.Column(db.String(5), unique=False, nullable=False)
    gpa = db.Column(db.Float, unique=False, nullable=False)
    def __init__(self, name, dep, gpa):
        self.name = name; self.dep = dep; self.gpa = gpa
    def __repr__(self):
        return self.name

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Student('John Rambo', 'it', 1.2))
    db.session.add(Student('Jack Ripper', 'cs', 4.0))
    db.session.add(Student('Joe Green', 'ee', 2.8))
    db.session.add(Student('Jame Bond', 'cs', 1.8))
    db.session.add(Student('Jim Jone', 'ce', 2.3))
    db.session.add(Student('Jimmy Swaggart', 'it', 3.1))
    db.session.add(Student('Jude Smart', 'cs', 3.8))
    db.session.add(Student('Judy Longer', 'it', 2.5))
    db.session.add(Student('Jerry Dame', 'cs', 3.5))
    db.session.add(Student('Janet Jubs', 'cs', 3.5))
    db.session.add(Student('Json Yang', 'cs', 3.5))
    db.session.add(Student('Jeronimo Down', 'ee', 1.5))
    db.session.commit()
admin.add_view(ModelView(Student, db.session))

# Custom Student View
class StudentView(ModelView):
    column_searchable_list = ('name',)
    column_filters = ('dep', 'gpa')
    
##    can_view_details = True
##    column_exclude_list = ['dep', ]

##    column_editable_list = ['name', 'dep']
    
##    can_delete = False
##    can_edit = False
##    can_create = False

##    can_export = True
##    export_types = ['csv', 'json']

##    page_size = 5  
##admin.add_view(StudentView(Student, db.session))

import os
if not os.path.exists('mydb.db'):
    init_db()



if __name__ == '__main__':
    app.run(port=8080, debug=True)

