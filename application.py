from flask import Flask
import socket

application = Flask(__name__)


@application.route('/')
def hello_world():
    return 'Welcome to my website'


@application.route('/getIP')
def get_ip():
    return "The host is {}".format(socket.gethostbyname(socket.gethostname()))


if __name__ == "__main__":
    application.run(debug=False)
