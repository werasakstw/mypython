from flask import Flask, render_template
from flask_admin import Admin

app = Flask(__name__)

# https://bootswatch.com/3/
# Try: cerulean, cosmo, cyborg, darkly, flatly, journal, 
# lumen, paper,readable, sandstone, simplex, slate, spacelab,
# superhero, united, yeti
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

admin = Admin(app, name='Main', template_mode='bootstrap3')

# Root index is \templates\index.html.
# Admin index is \templates\admin\index.html.
@app.route('/')
def index():
    return render_template('index.html')

# Root hello.
@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)
# http://127.0.0.1:8080/hello/john

if __name__ == '__main__':
   app.run(port=8080, debug=True)

# http://127.0.0.1:8080