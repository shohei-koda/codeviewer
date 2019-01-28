# coding: utf-8


import os
from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route('/')
def index():
    return 'テスト'

@app.route('/pycheck', methods=['POST'])
def pycheker():
    if request.headers['Content-Type'] == 'application/json':
        data = json.dumps(request.json)
        arrData = json.loads(data)

        for k, v in arrData:
            print(k)
            print(v)
            
        return 'git webhooks'

    return 'pycheck hello!'

if __name__ == '__main__':
    port = int(os.environ.get('FLASK_PORT', 5000))
    app.run(port=port)
