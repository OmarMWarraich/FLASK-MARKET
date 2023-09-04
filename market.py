from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route('/about/<username>')
def about(username):
    return f'<h1>This is the about Page of {username}</h1>'