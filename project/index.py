import RPi.GPIO as GPIO
import time

TRIG_PIN = 4
ECHO_PIN = 17  
led_pin = 21
buzzer_pin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(buzzer_pin,GPIO.OUT)
pwm = GPIO.PWM(buzzer_pin,392)
GPIO.setup(led_pin,GPIO.OUT)

try:
    while True:
        GPIO.output(TRIG_PIN, True)
        time.sleep(0.00001)  #10us (microsec)
        GPIO.output(TRIG_PIN, False)

        while GPIO.input(ECHO_PIN) == 0:
            pass
        start = time.time()  #ECHO PIN HIGH(상승시간)

        while GPIO.input(ECHO_PIN) == 1:
            pass
        stop = time.time()      #ECHO PIN LOW(하강시간)
   
        duration_time = stop - start        #전체 시간
        distance = duration_time * 17160        #34321/2

        print('Distance: %.1fcm' % distance)
        
        if distance <= 40:
            GPIO.output(led_pin,GPIO.HIGH)
            print('LED on')
        elif distance > 40:
            GPIO.output(led_pin,GPIO.LOW)
            print('LED off')
        if distance <=20 and distance>10:
            pwm.start(10) 
            time.sleep(0.5)
            pwm.ChangeDutyCycle(0)
            
        elif distance <=10:
            pwm.start(10)
            time.sleep(0.1)
            pwm.ChangeDutyCycle(0)
            time.sleep(0.1)
        
            
        time.sleep(0.1)

finally:
    pwm.stop()
    GPIO.cleanup()