from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello_world():
    return 'Hello this is new'


if __name__ == "__main__":
    application.run(debug=False)
