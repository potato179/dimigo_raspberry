from lcd import drivers
import time

display = drivers.Lcd()


cc = drivers.CustomCharacters(display)

cc.char_1_data = ["01001",
                  "10101",
                  "10101",
                  "10101",
                  "10101",
                  "10101",
                  "10101",
                  "01001"]
#이

cc.char_2_data = ["10101",
                  "11111",
                  "10101",
                  "11101",
                  "00000",
                "10000",
                "10000",
                "11111"]
#번

cc.char_3_data = ["01010",
                  "01011",
                  "10110",
                  "10110",
                  "00000",
                "10000",
                "10000",
                "11111"]
#산

cc.char_4_data = ["01001",
                  "11101",
                  "01011",
                  "10101",
                  "00000",
                  "10000",
                  "10000",
                  "11111"]
#천

cc.char_5_data = ["01011",
                  "11111",
                  "01011",
                  "10111",
                  "01000",
                  "01110",
                  "10001",
                  "01110"]
#행

cc.char_6_data = ["01001",
"01001",
"10101",
"10101",
"00000",
"10000",
"10000",
"11111"]
#신

cc.char_7_data = ["01110",
                  "10001",
                  "01110",
                  "11111",
                  "00100",
                  "11111",
                  "11111",
                  "11111"]
#울

cc.char_8_data = ["11101",
                  "00111",
                  "00101",
                  "00111",
                  "00000",
                  "01110",
                  "10001",
                  "01110"]
#경

cc.char_9_data = ["11111",
                  "00100",
                  "01010",
                  "10001",
                  "00000",
                  "11111",
                  "00100",
                  "00100"]
#주

cc.char_10_data = ["11111",
                  "10000",
                  "11111",
                  "00100",
                  "11111",
                  "01110",
                  "10001",
                  "01110"]
#동

cc.char_11_data = ["00011",
                  "11111",
                  "10011",
                  "10011",
                  "10011",
                  "10011",
                  "11111",
                  "00011"]
#대

cc.char_12_data = ["11111",
                  "00001",
                  "00001",
                  "00001",
                  "00000",
                  "11111",
                  "00100",
                  "00100"]
#구

cc.char_13_data = ["11101",
                  "00101",
                  "00101",
                  "00101",
                  "00000",
                  "11111",
                  "10001",
                  "11111"]
#김

cc.char_14_data = ["00001",
                  "11101",
                  "10101",
                  "10101",
                  "10101",
                  "10101",
                  "11101",
                  "00001"]
#미

cc.char_15_data = ["11101",
                  "01001",
                  "10111",
                  "10101",
                  "00000",
                  "10000",
                  "10000",
                  "11111"]
#전

cc.char_16_data = ["11110",
                  "00110",
                  "00111",
                  "01010",
                  "11100",
                  "01110",
                  "10001",
                  "01110"]
#광

cc.char_17_data = ["11101",
                  "10111",
                  "10101",
                  "11111",
                  "00000",
                  "01110",
                  "10001",
                  "01110"]
#명

cc.char_18_data = ["00001",
                  "01001",
                  "01001",
                  "10101",
                  "10111",
                  "10101",
                  "10101",
                  "00001"]
#서

cc.load_custom_characters_data()

try:
    print("Writing to display")
    display.lcd_display_string(" ", 1);

    #while True:
        #display.lcd_display_string("** WELCOME **", 2)
        #time.sleep(2)
        #display.lcd_display_string("   WELCOME   ", 2)
        #time.sleep(2)

    #str = '#include <stdio.h> int main() { printf("Hello world"); return 0; }'
    # str = '     {0x06}{0x02}-{0x05}{0x07}{0x08}-{0x09}{0x10}{0x11}-{0x12}{0x03}{0x11}{0x13}-{0x09}{0x14}-{0x15}{0x16}-{0x17}{0x06}-{0x04}{0x05}{0x04}  '
    str = "     Ulsan-Singyeongju-Dongdaegu-GimcheonGumi-Daejeon-Gwangmyeong-Seoul-Haengshin     "
    display.lcd_display_extended_string('14:30|{0x04}{0x05}|KTX|040', 1)

    while True:
        for i in range(-15, len(str) + 15):
            display.lcd_display_string('                ', 2)
            time.sleep(0.01)
            display.lcd_display_string(' ' * max(-i, 0) + str[max(i, 0):min(i+15, len(str))] + ' ', 2)
            time.sleep(0.07)

        time.sleep(0.1)
finally:
    print("Cleaning Up!")
    display.lcd_clear()