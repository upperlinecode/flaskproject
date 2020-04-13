# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from model import shout


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return "hello world"
