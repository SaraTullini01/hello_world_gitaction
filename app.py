from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    
    return "<center><h1>dovresti funzionare!</h1><br><p>ciaooo</p></center>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# from flask import Flask, render_template
# from datetime import datetime

# app = Flask(__name__)

# @app.route('/')
# def index():
#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     return render_template('index.html', current_time=current_time)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)