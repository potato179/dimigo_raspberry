import RPi.GPIO as GPIO     # 라즈베리파이 GPIO 관련 모듈을 불러옴
import time      #time 라이브러리의 sleep함수 사용

GPIO.setmode(GPIO.BCM)      # GPIO 핀들의 번호를 지정하는 규칙 설정

### 이부분은 아두이노 코딩의 setup()에 해당합니다
servo_pin = 6                   # 서보핀은 라즈베리파이 GPIO 12번핀으로 

GPIO.setup(servo_pin, GPIO.OUT)  # 서보핀을 출력으로 설정 
pwm = GPIO.PWM(servo_pin, 50)  # 서보핀을 PWM 모드 50Hz로 사용
pwm.start(0)  # 서보모터의 각도 0도 

try:                                    # 이 try 안의 구문을 먼저 수행하고
    while True:                         # 무한루프 시작: 아두이노의 loop()와 같음
        val = input('1:-90, 2:0, 3:+90, 9:Quit> ')
        if val == '1':
            pwm.ChangeDutyCycle(3.5)  #0도
        elif val == '2':
            pwm.ChangeDutyCycle(7.5) #90도
        elif val == '3':
            pwm.ChangeDutyCycle(12.5) #180도
        elif val == '9':
            break

### 이부분은 반드시 추가해주셔야 합니다.
finally:                                # try 구문이 종료되면
    GPIO.cleanup()                      # GPIO 핀들을 초기화