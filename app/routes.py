from app import app
from flask import request


@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'


@app.route('/symbol')
def api_symbols():
    return 'rest'


@app.route('/symbol/<symbolid>')
def get_symbol_fee(symbolid):
    return 'This fee is: ' + symbolid
