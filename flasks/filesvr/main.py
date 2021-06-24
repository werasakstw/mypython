from flask import Flask, request, make_response
from flask_admin import Admin
from flask_admin.contrib.fileadmin import FileAdmin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello123'
admin = Admin(app, name='Static Files', template_mode='bootstrap3')

class MyFileAdmin(FileAdmin):
    can_edit = False 
    can_delete = False
##    can_rename = False

##    can_mkdir = False
##    can_upload = False

##    allowed_extensions = ('txt', 'xml')	# For upload files.

import os.path as op
path = op.join(op.dirname(__file__), 'files')
admin.add_view(MyFileAdmin(path, None, name='Data'))

#-----------------------------------------------------
from myutil import read_file, get_file, to_content_type

@app.route('/get/<name>')
def get(name):
    print(name)
    return read_file('files/' + name)
# curl 127.0.0.1:8080/get/hello.txt
# curl 127.0.0.1:8080/get/hello.xml

import os
@app.route('/data/<name>')
def data(name):
    d = get_file(name)	## using image pool
    if d == 'error':
        return 'Fails'
    _, ext = os.path.splitext(name)
    res = make_response(d)
    res.headers['Content-Length'] = len(d)
    res.headers['Content-Type'] = to_content_type(ext)
    return res
# curl 127.0.0.1:8080/data/hi.txt -I
# http://127.0.0.1:8080/data/john.png
# http://127.0.0.1:8080/data/students.json
# http://127.0.0.1:8080/data/students.csv
# http://127.0.0.1:8080/data/students.xml

if __name__ == '__main__':
    app.run(port=8080, debug=True)