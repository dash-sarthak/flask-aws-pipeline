from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "flask-aws-pipeline under construction"


# Post req
@app.route("/convert", methods=["POST"])
def convert():
    return "This is POST request"


# Get req
@app.route("/pull", methods=["GET"])
def pull():
    return "This is GET request"


if __name__ == "__main__":
    app.run()
