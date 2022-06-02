import RPi.GPIO as GPIO
import time

TRIG_PIN = 4
ECHO_PIN = 14   
BUZZER_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)

GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
pwm = GPIO.PWM(BUZZER_PIN, 392)  #솔

try:
    while True:
        GPIO.output(TRIG_PIN, True) #초음파 1초동안 발사
        time.sleep(1)  #10us (microsec)
        GPIO.output(TRIG_PIN, False)

        while GPIO.input(ECHO_PIN) == 0:
            pass
        start = time.time()     #ECHO PIN HIGH(시작)

        while GPIO.input(ECHO_PIN) == 1:
            pass
        stop = time.time()

        duration_time = stop - start
        distance = duration_time * 17160        #34321/2

        print('Distance: %.1fcm' % distance)
        time.sleep(0.1)

        if distance <= 30:
            for i in range(3):
                pwm.start(10)
                time.sleep(1)
                print("piezo on")
                pwm.ChangeDutyCycle(0)
                time.sleep(1)
                
        elif distance <= 10:
            for i in range(3):
                pwm.start(10)
                time.sleep(0.5)
                print("piezo on")
                pwm.ChangeDutyCycle(0)
                time.sleep(0.5)
        else:
            pwm.ChangeDutyCycle(0)
            print("piezo off")

finally:
    pwm.stop()
    GPIO.cleanup()    