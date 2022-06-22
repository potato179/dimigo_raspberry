import RPi.GPIO as GPIO
import time

SEGMENT_PINS = [3, 4, 5, 6, 7, 12, 13]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)

data = [1, 1, 1, 1, 1, 1, 0]

try:
    for _ in range(3):
        for i in range(len(SEGMENT_PINS)):
            GPIO.output(SEGMENT_PINS[i], data[i])

        time.sleep(1)

        for i in range(len(SEGMENT_PINS)):
            GPIO.output(SEGMENT_PINS[i], GPIO.LOW)

        time.sleep(1)
finally:
    GPIO.cleanup()
    print('clean up and exit')

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