from flask import Flask

app = Flask(__name__)

@app.route('/')
def string_return():
    return '문자열 반환해야 합니당'

# 문자열 반환 테스트용
@app.route('/sick')
def breadpage():
   return '식빵맨'
