from flask import Flask, request
app = Flask(__name__)

@app.route('/student/list')
def list():
    return 'GET: all student'
# curl 127.0.0.1:8080/student/list

@app.route('/student/get/<id>')
def get(id):
    return 'GET: get student id: ' + id
# curl 127.0.0.1:8080/student/get/1

@app.route('/student/delete/<id>', methods=['DELETE'])
def delete(id):
    return 'DELETE: delete student id: ' + id
# curl 127.0.0.1:8080/student/delete/1 -X DELETE

@app.route('/student/update/<id>', methods=['POST'])
def update(id):
    name = request.form['name']
    return 'POST: update student id: ' + id + ' name: ' + name
# curl 127.0.0.1:8080/student/update/1 -X POST -d name=john

@app.route('/student/save', methods=['PUT'])
def put():
    id = request.form['id']
    name = request.form['name']
    return 'PUT: save student id: ' + id + ' name: ' + name
# curl 127.0.0.1:8080/student/save -X PUT -d "id=2&name=jack"

if __name__ == '__main__':
    app.run(port=8080, debug=True)
