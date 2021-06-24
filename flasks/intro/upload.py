
from flask import Flask, render_template, request
app = Flask(__name__)
app.config['MAX_CONTENT_PATH'] = 2048   # Max size of file to be uploaded.

@app.route('/')
def index():
    return render_template('upload_index.html')
# http://127.0.0.1:8080

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return 'File upload success'

if __name__ == '__main__':
    app.run(port=8080, debug=True)

