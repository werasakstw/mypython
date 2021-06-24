# pip install flask_admin

from flask import Flask
from flask_admin import Admin

app = Flask(__name__)
admin = Admin(app)

# The admin index is templates/admin/index.html.
# The built-in admin/master.html is the base html.

if __name__ == '__main__':
   app.run(port=8080, debug=True)

# http://127.0.0.1:8080/admin/