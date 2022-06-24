import RPi.GPIO as GPIO
import time

PIN_RED = 17
PIN_YELLOW = 27
PIN_GREEN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_RED, GPIO.OUT)
GPIO.setup(PIN_YELLOW, GPIO.OUT)
GPIO.setup(PIN_GREEN, GPIO.OUT)

for i in range(99999999999999):
    GPIO.output(PIN_RED, GPIO.HIGH)
    GPIO.output(PIN_YELLOW, GPIO.LOW)
    GPIO.output(PIN_GREEN, GPIO.LOW)
    print("RED ON")
    time.sleep(0.02)
    GPIO.output(PIN_RED, GPIO.LOW)
    GPIO.output(PIN_YELLOW, GPIO.HIGH)
    GPIO.output(PIN_GREEN, GPIO.LOW)
    print("YELLOW ON")
    time.sleep(0.02)
    GPIO.output(PIN_RED, GPIO.LOW)
    GPIO.output(PIN_YELLOW, GPIO.LOW)
    GPIO.output(PIN_GREEN, GPIO.HIGH)
    print("GREEN ON")
    time.sleep(0.02)
    print("---------------------------------")

GPIO.setup(PIN_RED, GPIO.OUT)
GPIO.setup(PIN_YELLOW, GPIO.OUT)
GPIO.setup(PIN_GREEN, GPIO.OUT)