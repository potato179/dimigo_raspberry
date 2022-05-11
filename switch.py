import RPi.GPIO as GPIO
import time

BUTTON_PIN = 12
LED_PIN = 3

GPIO.setmode(GPIO.BCM)

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        val = GPIO.input(BUTTON_PIN)
        print(val)
        GPIO.output(LED_PIN, val)
finally:
    GPIO.cleanup()