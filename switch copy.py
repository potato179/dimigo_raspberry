# 필요한 모듈을 불러옵니다. 
import RPi.GPIO as GPIO
import time

# 사용할 GPIO핀의 번호를 선정합니다.(BCM 모드)
LED_PIN=3
BUTTON_PIN = 12     # PIN 번호 설정

GPIO.setmode(GPIO.BCM)  # GPIO핀의 번호 모드 설정
GPIO.setup(BUTTON_PIN, GPIO.IN)  # 입력핀의 IN/OUT 설정
#GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   


try:
    while 1:       
        val = GPIO.input(BUTTON_PIN)
        print(val)
        time.sleep(0.1)
        
except KeyboardInterrupt:
    pass
    print("exit with ^C")
    GPIO.cleanup()
    exit()