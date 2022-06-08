import RPi.GPIO as GPIO

LED_PIN_1=3
LED_PIN_2=4
LED_PIN_3=17

BUTTON_PIN_1=12
BUTTON_PIN_2=16
BUTTON_PIN_3=20

GPIO.setmode(GPIO.BCM)

GPIO,setup(LED_PIN_1,GPIO.OUT)
GPIO.setup(BUTTON_PIN_1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO,setup(LED_PIN_2,GPIO.OUT)
GPIO.setup(BUTTON_PIN_2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO,setup(LED_PIN_3,GPIO.OUT)
GPIO.setup(BUTTON_PIN_3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        val=
        GPIO.input(BUTTON_PIN_1)
        print(val)
        GPIO.output(LED_PIN_1,val)

        val=
        GPIO.input(BUTTON_PIN_2)
        print(val)
        GPIO.output(LED_PIN_2,val)

        val=
        GPIO.input(BUTTON_PIN_3)
        print(val)
        GPIO.output(LED_PIN_3,val)
finally:
    GPIO.cleanup()