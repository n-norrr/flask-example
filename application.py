from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello_world():
    return 'Hello from AWS'


if __name__ == "__main__":
    application.run(debug=False)
