import time

from flask import Flask
from os import environ

app = Flask(__name__)


@app.route('/')
def hello():
    hostname = environ.get('HOSTNAME')
    return f'{hostname}'
