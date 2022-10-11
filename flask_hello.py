from flask import flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Flask, trash!</p>"

if __name__ == "__main__":
    app.run(host = "0.0.0.0")