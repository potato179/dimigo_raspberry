# 필요한 모듈을 불러옵니다. 
import RPi.GPIO as GPIO
import time

# 사용할 GPIO핀의 번호를 선정합니다.(BCM 모드)
BUTTON_PIN = 12     # PIN 번호 설정
BUTTON_PIN_2 = 8
BUTTON_PIN_3 = 15
LED_PIN = 17
LED_PIN_2 = 10
LED_PIN_3 = 3

GPIO.setmode(GPIO.BCM)  # GPIO핀의 번호 모드 설정
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)
GPIO.setup(LED_PIN_3, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   # LED 핀의 IN/OUT 설정
GPIO.setup(BUTTON_PIN_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


try:
    while 1:       
        GPIO.output(LED_PIN, GPIO.input(BUTTON_PIN))
        GPIO.output(LED_PIN_2, GPIO.input(BUTTON_PIN_2))
        GPIO.output(LED_PIN_3, GPIO.input(BUTTON_PIN_3))
        
        if GPIO.input(BUTTON_PIN) or GPIO.input(BUTTON_PIN_2) or GPIO.input(BUTTON_PIN_3):
            print(GPIO.input(BUTTON_PIN), GPIO.input(BUTTON_PIN_2), GPIO.input(BUTTON_PIN_3))
        time.sleep(0.1)
        
except KeyboardInterrupt:
    pass
    print("exit with ^C")
    GPIO.cleanup()
    exit()