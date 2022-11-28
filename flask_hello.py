from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("hello.html")

@app.route("/first")
def express_mansae():
    return "<h1>Express 만세!</h1><br><a href = '/'>돌아가</a>"

@app.route("/led")
def ledjoygo():
    return render_template("led.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0")