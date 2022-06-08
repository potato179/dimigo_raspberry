# 필요한 모듈을 불러옵니다. 
import RPi.GPIO as GPIO
import time

# 사용할 GPIO핀의 번호를 선정합니다.(BCM 모드)
led_R = 2     # PIN 번호 설정
led_G = 3
led_B = 4

GPIO.setmode(GPIO.BCM)  # GPIO핀의 번호 모드 설정
GPIO.setwarnings(False)   # 불필요한 warning 제거

GPIO.setup(led_R, GPIO.OUT)   # LED 핀의 IN/OUT 설정
GPIO.setup(led_G, GPIO.OUT)
GPIO.setup(led_B, GPIO.OUT)


# 10번 반복문 
for i in range(10):
    GPIO.output(led_R, 1)    # LED ON
    print("red")
    time.sleep(1)   # 1초동안 대기상태 
    GPIO.output(led_R, 0)    # LED OFF
    time.sleep(1)   # 1초동안 대기상태

    GPIO.output(led_G, 1)    # LED ON
    print("green")
    time.sleep(1)   # 1초동안 대기상태 
    GPIO.output(led_G, 0)    # LED OFF
    time.sleep(1)   # 1초동안 대기상태

    GPIO.output(led_B, 1)    # LED ON
    print("blue")
    time.sleep(1)   # 1초동안 대기상태 
    GPIO.output(led_B, 0)    # LED OFF
    time.sleep(1)   # 1초동안 대기상태

GPIO.cleanup()     # GPIO 설정 초기화 

