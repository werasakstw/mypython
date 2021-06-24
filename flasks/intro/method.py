from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('method_index.html')
# http://127.0.0.1:8080

# Flask supports GET, POST, PUT, DELETE and HAED request methods.
@app.route('/get')
def get():
    return 'That was a GET.'

@app.route('/formget')
def form_get():
    name = request.args['name'] 
    return 'Hello ' + name + ' that was a GET.'

@app.route('/post', methods=['POST'])
def post():
    name = request.form['name'] 
    return 'Hello ' + name + ' that was a POST.'

# A 'view' function may be mapped to more than one methods.
@app.route('/getpost', methods=['GET', 'POST'])
def get_post():
    # handle the POST request
    if request.method == 'POST':
        name = request.form.get('name')
        return 'Hello ' + name

    # otherwise handle the GET request
    return '''
<form method="POST">
Name: <input type="text" name="name">
<input type="submit" value="Post">
</form>'''

@app.route('/put', methods=['POST'])
def put():
    if request.form['_method'] == 'PUT':
    	name = request.form['name']
    	return 'Hello ' + name + ' that was a PUT.'
    return 'Invalid request'

@app.route('/delete', methods=['POST'])
def delete():
    if request.form['_method'] == 'DELETE':
    	name = request.form['name']
    	return 'Hello ' + name + ' that was a DELETE.'
    return 'Invalid request'

if __name__ == '__main__':
    app.run(port=8080, debug=True)


