from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Scale Me - This is just a sample app waiting to be scaled"

if __name__ == "__main__":
    app.run()
