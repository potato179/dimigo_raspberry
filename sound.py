import RPi.GPIO as GPIO
import keyboard
import time

BUZZER_pin = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_pin, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_pin, 262)
pwm.start(99)

i = 1

try:
    while 1:
        pwm.ChangeFrequency(i+1)
        print(i+1)
        if keyboard.is_pressed(80):
            i -= 1

        if keyboard.is_pressed(72):
            i += 1

finally:
    pwm.stop()
    GPIO.cleanup()