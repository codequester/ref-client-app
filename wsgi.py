from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Scale Me - This is just a sample app waiting to be scaled"

if __name__ == "__main__":
    application.run()
