import RPi.GPIO as GPIO
import time

BUZZER_pin = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_pin, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_pin, 262)
pwm.start(99)

for i in range(1000000):
    pwm.ChangeFrequency(i+1)
    print(i+1)
    time.sleep(0.00001)

for i in range(1000000):
    pwm.ChangeFrequency(1000000-i)
    print(1000000-i)
    time.sleep(0.00001)