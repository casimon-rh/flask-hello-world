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
        return "response: {}".format(requests.get(os.environ.get('SERVER_URL')).json())
    except Exception as ex:
        print(ex)
        return "error"

if __name__ == '__main__':
    app.run()

