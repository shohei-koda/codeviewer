# coding: utf-8


import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'テスト'

@app.route('/pycheck', methods=('GET', 'POST'))
def pycheker():
    if request.method == 'POST':
        return request.get_json()

    return 'pycheck hello!'

if __name__ == '__main__':
    port = int(os.environ.get('FLASK_PORT', 5000))
    app.run(port=port)
