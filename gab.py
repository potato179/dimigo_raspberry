import spidev
import time
import random

# SPI 인스턴스 생성
spi = spidev.SpiDev()

# SPI 통신 시작
spi.open(0, 0)  # bus:0, dev:0 (CE0:0, CE1:1)

# SPI 통신 속도 설정
spi.max_speed_hz = 100000

# 0~7까지 8개의 채널에서 SPI 데이터 읽기
def analog_read(channel):
    ret = spi.xfer2([1, (8 + channel)<<4, 0])
    adc_out = ((ret[1] & 3) << 8) + ret[2]
    return adc_out

try:
    while True:
        # 0번 채널에서 읽어온 SPI 데이터(0~1023)
        reading = analog_read(0)
        #reading = random.randrange(0,1024)
        # 전압수치로 변환
        voltage = reading * 3.3 / 1023
        print("Reading=%d, voltage=%f" % (reading, voltage))
        time.sleep(0.8)

finally:
    spi.close()