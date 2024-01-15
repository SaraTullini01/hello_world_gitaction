from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    str="dimmi che funzioni ti prego!\n non mi deludere!\n"
    return str

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
