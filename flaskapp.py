from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! \n v. 1.0'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
