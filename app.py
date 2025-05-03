# インストールした「flask」モジュールをインポートする
from flask import Flask

# インスタンス化する
app = Flask(__name__) #アンダースコア(_)をnameの左右にそれぞれ2つずつ書く

#ルーティング設定をする
@app.route('/')
def hello_world():
    return 'Welcome to Flask World'

if __name__ == "__main__": #最後に記述する
    app.run(debug=True)
