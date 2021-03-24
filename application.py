from flask import Flask

application = Flask(__name__)

os.environ.get("FLASK_APP")

@application.route('/')
def hello_world():
    return 'THIS WORKS HAHA LOL XD'




if __name__ == "__main__":
    application.run(debug=False)
