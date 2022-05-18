import RPi.GPIO as GPIO
import time

BUZZER_pin = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_pin, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_pin, 262)
pwm.start(50)

time.sleep(2)
pwm.ChangeDutyCycle(0)

pwm.stop()
GPIO.cleanup()