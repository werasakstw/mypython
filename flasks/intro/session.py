from flask import Flask, request, session, redirect, url_for, render_template 
app = Flask(__name__)
app.secret_key = 'Any strings would do.'

@app.route('/')
def index():
    if 'name' in session:
        name = session['name']
        return 'You are logged in as: ' + name + '<p/>' + \
               "<a href = '/logout'>Log out</a><p/>" + \
               "<a href = '/hello'>Hello</a>"
    return 'You are not logged in! <p/>' + \
	   '<h2><a href="/login">Log in</a></h2>'
# http://127.0.0.1:8080/

@app.route('/hello')
def hello():
    name = session['name']
    return render_template('hello.html', name=name)

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['name'] = request.form['name']
      return redirect(url_for('index'))
   return '''
<form action = "" method = "POST">
Name <input type="text" name="name"/>
<p><input type="submit" value="Login"/>
</form>
'''

@app.route('/logout')
def logout():
   session.pop('name', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=8080, debug=True)

