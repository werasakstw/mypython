from flask import Flask, render_template

app = Flask(__name__)

# Endpoints:


@app.route("/hello")
def hello():
    return 'Hello'

@app.route("/hi")
def hi():
    return 'Hi'

@app.route("/whatup")
def whatup():
    return 'What up?'

#-----------------------------------------------------------

@app.route("/buttons")
def buttons():
    return render_template('buttons.html')

@app.route("/button_group")
def button_group():
    return render_template('button_group.html')

@app.route("/navbar")
def navbar():
    return render_template('navbar.html')

@app.route("/inputs")
def inputs():
    return render_template('inputs.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)

# https://getbootstrap.com/docs/5.0/examples/
