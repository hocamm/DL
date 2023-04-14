
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def string_return():
    return "ML 서버 열심히 만들자"


@app.route('/sick')
def breadpage():
   return '식빵맨'

@app.route("/curry")
def curry():
    return '''<!DOCTYPE HTML><html>
  <head>
    <title>카레빵맨 이미지 받아랑!!!</title>
  </head>
  <body>
    <h1>Curry bread man</h1>
    <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrfTgmkoNaKpFBUZ_DmdzbkGc66dsch5CWYg&usqp=CAU"
  </body>
</html>'''




@app.route('/bread', methods=['GET'])
def test_get():
    bread_receive = request.args.get('breadname')
    return f'이것의 이름은 {bread_receive}'




