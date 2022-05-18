import RPi.GPIO as GPIO
import time

BUZZER_pin = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_pin, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_pin, 262)
pwm.start(99)

melody = [392, 494, 660, 880, 1174]

try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)

finally:
    pwm.stop()
    GPIO.cleanup()



