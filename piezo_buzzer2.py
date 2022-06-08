import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1)  #주파수 1
pwm.start(90)

scale = [ 1, 262, 294, 330, 349, 392, 440, 494 ]
melody = [ 1, 1, 5, 5, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1, \
            5, 5, 4, 4, 3, 3, 2, 5 ,5, 4, 4, 3, 3, 2, \
            1, 1, 5, 5, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1 ]

try:
    for i in range(0, 43):
        pwm.ChangeFrequency(scale[melody[i]])
        if i==6 or i==13 or i==20 or i==27 or i==34 or i==41:
            time.sleep(1)
        else:
            time.sleep(0.5)
    pwm.stop()

finally:
    GPIO.cleanup()