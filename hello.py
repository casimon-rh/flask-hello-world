# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/send')
def send():
    try:
        return "response: {}".format(requests.get(os.environ.get('SERVER_URL')).text)
    except Exception as ex:
        print(ex)
        return "error"

@app.route('/file/create')
def create_file():
    try:
        file = open(os.environ.get('FILE_URL'),"a")
        file.write("hello world")
        file.close()
        return "done"
    except Exception as ex:
        print(ex)
        return "error"

@app.route('/file/read')
def read_file():
    try:
        file = open(os.environ.get('FILE_URL'),"r")
        return file.read()
    except Exception as ex:
        print(ex)
        return "error"

if __name__ == '__main__':
    app.run()

