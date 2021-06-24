from flask import Flask, render_template, redirect, request, session, url_for, flash
from flask_login import LoginManager, login_required, \
	UserMixin, login_user, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite'
app.config['USE_SESSION_FOR_NEXT'] = True
db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    pwd = db.Column(db.String(20), nullable=False)
    def __repr__(self):
        return self.name 

db.drop_all()
db.create_all()
hpwd = generate_password_hash('john', method='sha256')
db.session.add(User(name='john', pwd=hpwd))
hpwd = generate_password_hash('jack', method='sha256')
db.session.add(User(name='jack', pwd=hpwd))
db.session.commit()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lists')
def lists():
    return str( User.query.all() )

@app.route('/curuser')
def curuser():
    try:
        return current_user.name
    except:
        return 'None'

@app.route('/hello')
@login_required
def hello():
    return 'Hello ' + current_user.name

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    name = request.form.get('name')
    pwd = request.form.get('pwd')
    if name == '' or pwd == '':
        flash('Name and password are required.')
        return redirect(url_for('login'))

    user = User.query.filter_by(name=name).first()
    if not user or not check_password_hash(user.pwd, pwd):
        flash('Invalid user or password.')
        return redirect(url_for('login')) 
    login_user(user, remember=True)

    if 'next' in session:
        return redirect(session['next'])
    return user.name + ' successfully login.'

@app.route('/logout')
@login_required
def logout():
    tmp = current_user.name
    logout_user()
    return tmp + ' logout.'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    name = request.form.get('name')
    pwd = request.form.get('pwd')
    cpwd = request.form.get('cpwd')
    if name == '' or pwd == '' or cpwd == '':
        flash('Name, password and comfirm password are required.')
        return redirect(url_for('register'))
    if pwd != cpwd:
        flash('Confirm password in valid.')
        return redirect(url_for('register'))

    user = User.query.filter_by(name=name).first()
    if user:
        flash('The user is already registered.')
        return redirect(url_for('register'))

    hpwd = generate_password_hash(pwd, method='sha256')
    db.session.add(User(name=name, pwd=hpwd))
    db.session.commit()
    flash('Register success.')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8080, debug=True)