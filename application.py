from flask import Flask
import socket

application = Flask(__name__)


@application.route('/')
def hello_world():
    return "The host is {}".format(socket.gethostbyname(socket.gethostname()))


if __name__ == "__main__":
    application.run(debug=False)
