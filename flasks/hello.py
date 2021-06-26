# pip install flask

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

if __name__ == '__main__':
    app.run()	   	# http://127.0.0.1:5000
