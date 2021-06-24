# pip install flask-login

from flask import Flask
from flask_login import LoginManager, login_required

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app) 

@app.route('/hello')
def hello():
    return 'Hello'
# http://127.0.0.1:8080/hello

@app.route('/hi')
@login_required
def hi():
    return 'Hi'
# http://127.0.0.1:8080/hi

if __name__ == '__main__':
    app.run(port=8080, debug=True)