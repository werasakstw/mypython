# pip install flask

from flask import Flask
app = Flask(__name__)
'''
A route path is mapped to a 'view' function by annotation.
Flask dispaths requests to 'view' function according to the route path.
'''
@app.route('/')        # route() is a Flask decorator.
@app.route('/index')   # A 'view' function may have more than one route paths.
def index_():          # The function name may not be the same as route path.
    return 'Hello I am index.'

@app.route('/hello')
def hello():
    return 'Hello!'

'''
Parameters to 'view' functions can be passed in the request path.
The parameter names are denote as <variable> which must be the
same as parameters to the 'view' function.'''
@app.route('/hi/<name>')
def hi(name):
    return 'Hi ' + name

'''
Parameters are str by default.
But can be type annotated as 'int' or 'float'.
A view function must return str, dict, tuple, Response, or WSGI callable.'''
@app.route('/add/<int:x>/<int:y>')
def add(x, y):
    return str(x + y)

#-----------------------------------------------------------

if __name__ == '__main__':
##    app.run()	   	# http://127.0.0.1:5000
##    app.run(port=80)  # http://localhost
##    app.debug = True
    app.run(port=8080, debug=True) # http://127.0.0.1:8080

'''  app.run(host, port, debug, options)
host: Defaults is 127.0.0.1 (localhost). 
      Set to ‘0.0.0.0’ to have server available externally
port: Defaults is 5000.
debug: Defaults is False.
options: To be forwarded to underlying Werkzeug server.'''

# http://127.0.0.1:8080             curl 127.0.0.1:8080
# http://127.0.0.1:8080/hello       curl 127.0.0.1:8080/hello
# http://127.0.0.1:8080/hi/john
# http://127.0.0.1:8080/add/1/2
