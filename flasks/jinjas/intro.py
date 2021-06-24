from flask import Flask, render_template
app = Flask(__name__)

# Flask comes with jinja engine.
# 'Template' is used for wrapping jinja string.
from jinja2 import Template
@app.route('/temp/<n>')
def temp(n):
    s ='Hello {{ name }} how do you do?'
    return Template(s).render(name=n)
# curl 127.0.0.1:8080/temp/John

# Jinja can be mixed with HTML.
# Render HTML template.
@app.route('/hello/<n>')
def hello(n):
    return render_template('hello.html', name=n)
# curl 127.0.0.1:8080/hello/Jack

a = ['john', 'jack', 'joe']

# Import Macro
@app.route("/macro")
def macro(): 
     return render_template('macro.html', names=a)
# http://127.0.0.1:8080/macro

# Base and extend template.
@app.route("/base")
def base(): 
    return render_template('base_index.html')
# http://127.0.0.1:8080/base

if __name__ == '__main__':
    app.run(port=8080, debug=True) 
