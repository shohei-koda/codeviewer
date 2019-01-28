# coding: utf-8


import os
import pprint
import subprocess
from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route('/')
def index():
    return 'テスト'

@app.route('/pycheck', methods=['POST'])
def pycheker():
    if request.headers['Content-Type'] == 'application/json':
        code_dir = '/tmp/test_code'


        data = json.dumps(request.json)
        arrData = json.loads(data)

        #pprint.pprint(arrData['repository']['clone_url'])
        pprint.pprint(arrData.keys())
        clone_url = arrData['repository']['clone_url']
        cmd = f'git clone {clone_url} {code_dir}'

        """
        proc = subprocess.Popen(cmd, shell=True)

        try:
            outs,err = proc.communicate(timeout=15)
        except TimeoutExpired:
            proc.kill()
        """
        proc = subprocess.run(['git', 'clone', clone_url, code_dir], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print('git cloned')
        print(proc.stdout.decode('utf8'))
        print(proc.stderr.decode('utf8'))

        proc = subprocess.run(['flake8', code_dir], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print('exec flake8')
        print(proc.stdout.decode('utf8'))
        print(proc.stderr.decode('utf8'))

            
        return 'git cloned'

    return 'pycheck hello!'

if __name__ == '__main__':
    port = int(os.environ.get('FLASK_PORT', 5000))
    app.run(port=port)
