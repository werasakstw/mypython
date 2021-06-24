from flask import Flask, url_for
app = Flask(__name__)

@app.route("/hello")
def hello():
    print('hello')
    return 'Hello'
# curl 127.0.0.1:8080/hello

@app.before_first_request
def before_first_request():
    print('Before First Request')

@app.before_request
def before_request():
    print('Before Request')

@app.after_request
def after_request(res):
    print('After Request')
    return res

if __name__ == '__main__':
    app.run(port=8080, debug=True)

# curl 127.0.0.1:8080/hello

