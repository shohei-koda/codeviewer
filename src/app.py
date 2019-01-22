
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'テスト'

@app.route('/pycheck')
def pycheker():
    return 'pycheck';


if __name__ == '__main__':
    app.run()
