from flask import Flask, request # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask!"

@app.route('/data', methods=['POST'])
def data():
    return{
    "name":"Bob",
    "age" : 24,
    "gokul":request.json
    }

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)