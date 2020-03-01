from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about_me():
    return render_template('about.html')

# using jinja, the decorator can take an arg to pass to func
@app.route('/<username>')
def hello_name(username=None):
    return render_template('index.html', name=username)