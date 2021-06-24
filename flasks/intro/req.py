from flask import Flask, render_template, request
app = Flask(__name__)

''' When a Flask web server gets a connection from client,
it creates a request context and dispatches to a view function.

A 'request' has information about the request as attributes and
request headers in the 'header' attribute(as a dict).
A 'request' has lifetime of of the request. '''
@app.route('/requrl/<p>')
def requrl(p):
    d = {}
    d['url'] = request.url
    d['base_url'] = request.base_url
    d['scheme'] = request.scheme
    d['host'] = request.host
    d['remote_addr'] = request.remote_addr
    d['method'] = request.method
    d['path'] = request.path
    d['full_path'] = request.full_path
    d['query_string'] = request.query_string.decode()
    d['is_secure'] = str(request.is_secure)
    d['endpoint'] = request.endpoint
    d['p'] = p
    return d
# http://127.0.0.1:8080/requrl/john
# http://127.0.0.1:8080/requrl/reqpath?name=john&id=1

@app.route('/headers')
def headers():
    return dict(request.headers)
# http://127.0.0.1:8080/headers

if __name__ == '__main__':
    app.run(port=8080, debug=True)
