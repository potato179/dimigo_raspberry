import RPi.GPIO as GPIO
import time

PIN_LED = 12
GPIO.setmode(GPIO.BCM) 
GPIO.setup(PIN_LED, GPIO.OUT)   
pwm = GPIO.PWM(PIN_LED, 50)  #주파수 50hz

try:
    while 1:
        pwm.start(0)  #duty_cycle (0~100)  
        time.sleep(1)
        pwm.ChangeDutyCycle(25)
        time.sleep(1)
        pwm.ChangeDutyCycle(50)
        time.sleep(1)
        pwm.ChangeDutyCycle(100)
        time.sleep(1)
finally:
    pwm.stop()
    GPIO.cleanup()
