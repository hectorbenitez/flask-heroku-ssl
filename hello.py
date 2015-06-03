import os
from flask import Flask
from flas.decorators import ssl_required
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route('/')
@ssl_required
def hello():
    return 'Hello World!'
