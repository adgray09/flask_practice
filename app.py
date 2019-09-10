import requests
from flask import Flask

app = Flask(__name__)

@app.route('/joke')
def make_joke():
    params