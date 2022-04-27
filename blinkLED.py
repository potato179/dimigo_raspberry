import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED_PIN = 4
GPIO.setup(LED_PIN, GPIO.OUT)

while True : 
    GPIO.output(LED_PIN, True)
    time.sleep(0.1)
    GPIO.output(LED_PIN, False)
    time.sleep(0.1)
