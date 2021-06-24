from flask import Flask
from flask_login import LoginManager, login_required, \
	UserMixin, login_user, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite'
db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

db.drop_all()
db.create_all()
db.session.add(User(name='john'))
db.session.add(User(name='jack'))
db.session.commit()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))

@app.route('/login/<name>')
def login_(name):
    user = User.query.filter_by(name=name).first()
    login_user(user)
    return user.name + ' login.'

@app.route('/info')
@login_required
def info():
    return 'Current user is ' + current_user.name

@app.route('/logout')
@login_required
def logout():
    tmp = current_user.name
    logout_user()
    return tmp + ' logout.'

if __name__ == "__main__":
    app.run(port=8080, debug=True)