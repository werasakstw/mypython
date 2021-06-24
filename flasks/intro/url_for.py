from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.route('/hello')	      # An end points for creating url.
def hello():
    return 'Hello how are you?'

@app.route('/for_hello')
def for_hello():
    return url_for('hello')    # map to 'view' function, not route path
# curl 127.0.0.1:8080/for_hello

@app.route('/for_hello_ext')
def for_hello_ext():
    return url_for('hello', _external=True)  # Full url path
# curl 127.0.0.1:8080/for_hello_ext

@app.route('/hi/<name>')
def hi(name):
    return 'Hi ' + name

@app.route('/for_hi/<name>')
def for_hi(name):
    return url_for('hi', name=name)
# curl 127.0.0.1:8080/for_hi/john

@app.route('/hello_test')
def hello_test():
    u = url_for('hello', name='john')
    return '<a href=%s>Hello</a>' % u
# http://127.0.0.1:8080/hello_test

@app.route('/redir')
def redir():
    return redirect(url_for('hello'))
# http://127.0.0.1:8080/redir

# Url for static resources.
@app.route('/static')
def for_static():
    return url_for('static', filename='john.png')
# http://127.0.0.1:8080/static

if __name__ == '__main__':
    app.run(port=8080, debug=True)

