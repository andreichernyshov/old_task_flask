from flask import Flask
app=Flask(__name__)

@app.route('/')
def index_page():
    return '<h1>Index page</h1>'


@app.route('/hello')
def hello_world():
    return '<h2>Hello, World!</h2>'


