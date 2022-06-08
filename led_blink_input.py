# 필요한 모듈을 불러옵니다. 
import RPi.GPIO as GPIO
import time

# 사용할 GPIO핀의 번호를 선정합니다.(BCM 모드)
PIN_LED = 4     # PIN 번호 설정
GPIO.setmode(GPIO.BCM)  # GPIO핀의 번호 모드 설정
GPIO.setup(PIN_LED, GPIO.OUT)   # LED 핀의 IN/OUT 설정
GPIO.setwarnings(False)   # 불필요한 warning 제거

# 10번 반복문 
for i in range(10):
    inp = int(input("1:on, 0:off > "))
    if inp==1:
        GPIO.output(PIN_LED, 1)    # LED ON
        print("LED on")
        time.sleep(1)   # 1초동안 대기상태
    elif inp==0:
        GPIO.output(PIN_LED, 0)    # LED OFF
        print("LED off")
        time.sleep(1)   # 1초동안 대기상태
    else:
        print("clean up and exit.")
        GPIO.cleanup()     # GPIO 설정 초기화  
        break
   



