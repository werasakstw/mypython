from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('param_index.html')
# http://127.0.0.1:8080/

@app.route('/pathparam/<id>/<name>')
def pathparam(id, name):
    d = {}
    d['id'] = id
    d['name'] = name
    return d
# http://127.0.0.1:8080/pathparam/1/john

@app.route('/querystr')
def querystr():
    d = {}
    d['id'] = request.args['id']         # error 400 if no 'id'.
    d['name'] = request.args.get('name') # None if no 'name'.
    return d
# http://127.0.0.1:8080/querystr?name=jack&id=2

@app.route('/form', methods=['POST'])
def form():
    d = {}
    d['id'] = request.form['id']
    d['name'] = request.form.get('name')
    return d
# curl 127.0.0.1:8080/form -X POST -d "id=4&name=jame"
# curl 127.0.0.1:8080/form -X POST -d "id=4&name=Jame Bond"

if __name__ == '__main__':
    app.run(port=8080, debug=True)
