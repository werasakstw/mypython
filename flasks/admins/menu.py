from flask import Flask, render_template
from flask_admin import Admin, BaseView, expose
from flask_admin.menu import MenuLink

app = Flask(__name__)
admin = Admin(app, name='My App', template_mode='bootstrap3')

@app.route('/hello')
def hello():
    return '<h1>I am hello().</h1>'

# Links
admin.add_link(MenuLink(name='Google', url='http://google.com', category='Links'))
admin.add_link(MenuLink(name='Hello', url='/hello', category='Links'))

# Tap
class MyView(BaseView):
    @expose('/')
    def index(self):
        return 'I am MyView.'
admin.add_view(MyView(name='My View', \
     menu_icon_type='glyph', menu_icon_value='glyphicon-home'))

# Menu
class HelloView(BaseView):
    @expose('/')
    def index(self):
        return render_template('hello.html', name='Jack')

class HiView(BaseView):
    @expose('/')
    def index(self):
        return 'I am HiView.'
admin.add_view(HelloView(name='Hello', category='Greeting'))
admin.add_view(HiView(name='Hi', category='Greeting'))

# View Page
class GreetView(BaseView):
    @expose('/')
    def index(self):
        return self.render('greet.html')

    @expose('/formal')
    def formal(self):
        return 'Hello I am formal().'

    @expose('/informal')
    def informal(self):
        return 'Hi I am informal().'
admin.add_view(GreetView(name="Greet View"))

if __name__ == '__main__':
   app.run(port=8080, debug=True)

# http://127.0.0.1:8080/admin