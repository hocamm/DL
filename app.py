from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '손흥민 폼 미쳤다'

app.run(host = '127.0.0.1', port=8080)

app.config.from_object('satcounter_config')