# pip install flask-sqlalchemy

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db = SQLAlchemy(app)

class SqStudent(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    dep = db.Column(db.String(5), unique=False, nullable=False)
    gpa = db.Column(db.Float, unique=False, nullable=False)
    def __repr__(self):
        return '{"sid": %s, "name": "%s", "dep": "%s", "gpa": %s }' % \
                (self.sid, self.name, self.dep, self.gpa)

@app.route('/student/init')      
def SqStudent_init():
    db.create_all()
    db.session.add( SqStudent(name='john', dep='ce', gpa=1.8) )
    db.session.add( SqStudent(name='jack', dep='cs', gpa=4.0) )
    db.session.add( SqStudent(name='joe', dep='cs', gpa=2.8) )
    db.session.add( SqStudent(name='jame', dep='it', gpa=1.3) )
    db.session.commit()
    return 'Init success'
# curl 127.0.0.1:8081/student/init

@app.route('/student/list')
def SqStudent_list():
    return str( SqStudent.query.all() )
# curl 127.0.0.1:8081/student/list

@app.route('/student/get/<sid>')
def SqStudent_get(sid):
    return str( SqStudent.query.get(sid) )
# curl 127.0.0.1:8081/student/get/1

@app.route('/student/save', methods=['PUT'] )
def SqStudent_save():
    sid = request.form.get('sid')
    name = request.form.get('name')
    dep = request.form.get('dep')
    gpa = request.form.get('gpa')
    db.session.add( SqStudent(name=name, dep=dep, gpa=gpa) )
    db.session.commit()
    return 'Save success'
# curl 127.0.0.1:8081/student/save -X PUT -d "sid=1&name=jim&dep=ee&gpa=1.2"

@app.route('/student/update/<sid>', methods=['POST'] )
def SqStudent_update(sid):
    s = SqStudent.query.get(sid)
    if s == None:
        return 'Invalid sid'
    name = request.form.get('name')
    if name != None:
        s.name = name
    dep = request.form.get('dep')
    if dep != None:
        s.dep = dep
    gpa = request.form.get('gpa')
    if gpa != None:
        s.gpa = float(gpa)
    db.session.commit()
    return 'Update success'
# curl 127.0.0.1:8081/student/update/5 -X POST -d gpa=3.2

@app.route('/student/delete/<sid>', methods=['DELETE'] )
def SqStudent_delete(sid):
    SqStudent.query.filter(SqStudent.sid==sid).delete()
    db.session.commit()
    return 'Delete success'
# curl 127.0.0.1:8081/student/delete/5 -X DELETE

if __name__ == '__main__':
    app.run(port=8081, debug=True)
