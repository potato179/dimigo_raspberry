import RPi.GPIO as GPIO
import time

BUTTON_PIN1 = 4
BUTTON_PIN2 = 17
BUTTON_PIN3 = 27
LED_PIN1 = 18
LED_PIN2 = 23
LED_PIN3 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN3, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(LED_PIN3, GPIO.OUT)

try:
    while True:
        val1 = GPIO.input(BUTTON_PIN1) 
        val2 = GPIO.input(BUTTON_PIN2)
        val3 = GPIO.input(BUTTON_PIN3)
        GPIO.output(LED_PIN1,val1)
        GPIO.output(LED_PIN2,val2)
        GPIO.output(LED_PIN3,val3)
        print(val1, val2, val3)
finally:
    GPIO.cleanup()