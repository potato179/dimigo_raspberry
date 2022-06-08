import RPi.GPIO as GPIO
import time

TRIG_PIN = 4
ECHO_PIN = 14   
PIN_LED = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.output(TRIG_PIN, False)
time.sleep(2)

try:   
    while True:
        GPIO.output(TRIG_PIN, True)
        time.sleep(0.00001)  #10us (microsec)
        GPIO.output(TRIG_PIN, False)

        while GPIO.input(ECHO_PIN) == 0:
            start = time.time()     #ECHO PIN HIGH(상승시간)

        while GPIO.input(ECHO_PIN) == 1:
            stop = time.time()      #ECHO PIN LOW(하강시간)
    
        duration_time = stop - start        #전체 시간
        distance = duration_time * 17160        #34321/2

        print('Distance: %.1fcm' % distance)
        time.sleep(0.2)     #0.1초 간격으로 센서 측정

        if distance <= 20:
            GPIO.output(PIN_LED, 1)    # LED ON
            print("LED on")
        else:
            GPIO.output(PIN_LED, 0)    # LED OFF
            print("LED off")

finally:
    GPIO.cleanup()    