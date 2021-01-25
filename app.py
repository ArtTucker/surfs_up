from flask import Flask
app = Flask(__name__)
@app.route('/')

def hello_world():
    name = input("What's your name?")
    return 'Hello, '+name+'!'
