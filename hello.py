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
    result = ""
    try:
        if(not os.environ.get('CERTS_URL') or not os.environ.get('CA_URL')):
            result = "response: {}".format(
                requests.get(os.environ.get('SERVER_URL')).text)
        else:
            result = "response: {}".format(requests.get(
                os.environ.get('SERVER_URL'),
                verify=os.environ.get('CA_URL'),
                cert=(
                    "{}/client.crt".format(os.environ.get('CERTS_URL')),
                    "{}/client.key".format(os.environ.get('CERTS_URL'))
                )
            ).text)
        return result
    except Exception as ex:
        print(ex)
        return "error"


@app.route('/file/create')
def create_file():
    try:
        file = open(os.environ.get('FILE_URL'), "a")
        file.write("hello world")
        file.close()
        return "done"
    except Exception as ex:
        print(ex)
        return "error"


@app.route('/file/read')
def read_file():
    try:
        file = open(os.environ.get('FILE_URL'), "r")
        return file.read()
    except Exception as ex:
        print(ex)
        return "error"


if __name__ == '__main__':
    app.run()
