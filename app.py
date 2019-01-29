# coding: utf-8

import os
import pprint
import subprocess
import requests

from flask import Flask, render_template, request, json


app = Flask(__name__)


@app.route('/')
def index():
    return 'テストへようこそ！'

@app.route('/pycheck', methods=['POST'])
def pycheker():
    # コンテンツタイプで判断
    if request.headers['Content-Type'] == 'application/json':
        # git clone先
        code_dir = '/app'

        # リクエストデータのjsonを辞書型に変換
        data = json.dumps(request.json)
        arrData = json.loads(data)

        #pprint.pprint(arrData['repository']['clone_url'])
        pprint.pprint(arrData.keys())

        # リクエストデータからクローンURLを取得
        clone_url = arrData['repository']['clone_url']
        # リクエストデータからレビューコメント追加URLを取得
        review_url = arrData['pull_request']['url']
        review_url = f'{review_url}/reviews/1/events'


        """
        コマンド実行方法　別解

        cmd = f'git clone {clone_url} {code_dir}'
        proc = subprocess.Popen(cmd, shell=True)

        try:
            outs,err = proc.communicate(timeout=15)
        except TimeoutExpired:
            proc.kill()
        """

        """ コマンド実行 git clone & flake8 """
        proc = subprocess.run(['git', 'clone', clone_url, code_dir], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print('git cloned')
        print(proc.stdout.decode('utf8'))
        print(proc.stderr.decode('utf8'))

        proc = subprocess.run(['flake8', code_dir], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print('exec flake8')
        print(proc.stdout.decode('utf8'))
        print(proc.stderr.decode('utf8'))

        postData = {'body': 'comment review. @todo transiton to check runs event', 'event': 'COMMENT'}
        ret = requests.post(review_url, data=postData)

        print(review_url)
        print(ret)

            
        return 'git cloned'

    return 'pycheck hello!'

if __name__ == '__main__':
    port = int(os.environ.get('FLASK_PORT', 5000))
    app.run(port=port)
