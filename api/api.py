from flask import Flask

app = Flask(__name__)

@app.route('/greet')
def greet():
    return {
        "name": "Susheel",
        "age":25,
        "place": "Bangalore"
    }