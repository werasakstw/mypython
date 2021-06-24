from flask import Flask, render_template, redirect, make_response, abort, url_for
app = Flask(__name__)

# Raw txt.
@app.route('/txt')
def txt():
    return 'I am rawtxt.'
# curl 127.0.0.1:8080/txt

# Raw HTML.
@app.route('/html')
def html():
    return '<html><body><h1>I am rawhtml.</h1></body></html>'
# http://127.0.0.1:8080/html

# Raw text with respond code.
@app.route('/raw/<name>')
def raw(name):
    if name == 'John':
        abort(404) 		 # Not Found
    if name == 'Jack':
        return 'Bad name', 400	 # Bad request	 
    return 'Hello ' + name, 200	 # OK (default).
# http://127.0.0.1:8080/raw/John
# http://127.0.0.1:8080/raw/Jack
# http://127.0.0.1:8080/raw/Joe

@app.route('/maketxt')
def maketxt():
    s = 'Hello how do you do?'
    res = make_response(s)
    res.set_cookie('mycookie', '1')
    res.headers['Content-Length'] = len(s)
    res.headers['Content-Type'] = 'text/html'
    res.headers['X-Parachutes'] = 'I am John.'
    return res
# http://127.0.0.1:8080/maketxt
# curl http://127.0.0.1:8080/maketxt -i

@app.route('/makehtml')
def makehtml():
    r = make_response(render_template('hello.html', name='Jack'))
    r.headers['X-Parachutes'] = 'I am Jack.'
    return r
# http://127.0.0.1:8080/makehtml
# curl http://127.0.0.1:8080/makehtml -i

# Render with template.
@app.route('/temp/<name>')
def temp(name):
    return render_template('hello.html', name=name)
# http://127.0.0.1:8080/temp/Joe

# Render with redirection.
@app.route('/redir')
def redir():
    # return redirect('http://www.google.com')
    return redirect(url_for('temp', name='Jame')) # 'temp' is the view function.
# http://127.0.0.1:8080/redir

# Render static
@app.route("/static")
def static_():
   return render_template("js.html")
# http://127.0.0.1:8080/static

if __name__ == '__main__':
    app.run(port=8080, debug=True) 



