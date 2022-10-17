from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Flask, trash!</h1><br><a href = '/first'>I love Express</a>"

@app.route("/first")
def express_mansae():
    return "<h1>Express 만세!</h1><br><a href = '/'>돌아가</a>"

if __name__ == "__main__":
    app.run(host = "0.0.0.0")