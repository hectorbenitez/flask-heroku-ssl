import os
from flask import Flask
from flas.decorators import ssl_required

app = Flask(__name__)

@app.route('/')
@ssl_required
def hello():
    return 'Hello World!'
