from flask import Flask, flash, request, redirect, url_for, render_template 
app = Flask(__name__)
app.secret_key = 'Hello how do you do?'

@app.route('/')
def index():
    return render_template('flashes_index.html')
# http://127.0.0.1:8080/

from time import localtime
def get_time():
    return '%02d:%02d:%02d' % localtime()[3:6]

@app.route('/setflash')
def setflash():
    flash('Hello '+ get_time())
    return render_template('flashes_index.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)

