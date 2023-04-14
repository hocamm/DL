from flask import Flask

app = Flask(__name__)

@app.route('/')
def string_return():
    return '문자열 반환해야 합니당'

# 문자열 반환 테스트용
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
