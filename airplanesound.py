import RPi.GPIO as GPIO
import time

BUZZER_pin = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_pin, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_pin, 262)
pwm.start(99)

try:
    for i in range(5000):
        pwm.ChangeFrequency(i+1)
        print((i+1)/10, "km/h")
        time.sleep(0.01)

finally:
    pwm.stop()
    GPIO.cleanup()