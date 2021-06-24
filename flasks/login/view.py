from flask import Flask, request
from flask_login import LoginManager, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello123'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# A login hook.
@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'Login'

@login_manager.user_loader
def load_user(uid):
    return None

@app.route('/hello')
def hello():
    return 'Hello'
# http://127.0.0.1:8080/hello	 No need to login.

@app.route('/hi')
@login_required
def hi():
    return 'Hi'
# http://127.0.0.1:8080/hi	 Login required.

if __name__ == "__main__":
    app.run(port=8080, debug=True)