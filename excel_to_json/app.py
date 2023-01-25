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

<<<<<<< Updated upstream

if __name__ == "__main__":
    app.run()
=======
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    
>>>>>>> Stashed changes
