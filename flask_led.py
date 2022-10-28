from flask import Flask
import RPi.GPIO as GPIO 

PIN_LED = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def hello():
    return '''<p>Flask, trash!</p>
        <a href = '/led/on'> on</a>
        <a href = '/led/off'> off</a>
        <a href = '/asdf'> asdf</a>
    '''

@app.route("/led/on")
def on():
    GPIO.output(PIN_LED, True)
    return "on page <a href = '/'> home</a>"

@app.route("/led/off")
def off():
    GPIO.output(PIN_LED, False)
    return "off page <a href = '/'> home</a>"

@app.route("/asdf")
def asdf():
    return "asdf page <a href = '/'> home</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")