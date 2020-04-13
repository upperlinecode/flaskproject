from flask import render_template, request
from model import shout

@app.route('/')
@app.route('/index')
def index():
    return "hello world"
