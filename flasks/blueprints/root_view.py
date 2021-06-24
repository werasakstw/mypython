from flask import Blueprint, request
root = Blueprint('root', __name__)

@root.route('/')
def index():
    return 'Root index.'
# curl 127.0.0.1:8080

@root.route('/hello/<name>')
def hello(name):
    return 'Hello ' + name + ' I am hello.'
# curl 127.0.0.1:8080/hello/John


