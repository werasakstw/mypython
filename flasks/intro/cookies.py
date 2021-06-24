from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('cookies_index.html')
# http://127.0.0.1:8080/

@app.route('/setcookies', methods = ['POST', 'GET'])
def setcookies():
    if request.method == 'POST':
        name = request.form['name']
   
    res = make_response('<a href="/getcookies">Get Cookies</a>')
    res.set_cookie('name', name)
    return res

@app.route('/getcookies')
def getcookies():
   name = request.cookies.get('name')
   return 'name: ' + name

if __name__ == '__main__':
    app.run(port=8080, debug=True)
