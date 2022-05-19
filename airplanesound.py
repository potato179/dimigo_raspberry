import RPi.GPIO as GPIO
import time

BUZZER_pin = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_pin, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_pin, 262)
pwm.start(99)

for i in range(10000000000000000000000000000000000000000000000000000):
    pwm.ChangeFrequency(i+1)
    print("BJS speed", i+1, "km/h")
    time.sleep(0.00000001)