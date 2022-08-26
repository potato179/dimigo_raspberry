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

cc.char_2_data = ["10101",
                  "11111",
                  "10101",
                  "11101",
                  "00000",
                "10000",
                "10000",
                "11111"]

cc.char_3_data = ["01010",
                  "01011",
                  "10110",
                  "10110",
                  "00000",
                "10000",
                "10000",
                "11111"]

cc.char_4_data = ["01001",
                  "11101",
                  "01011",
                  "10101",
                  "00000",
                  "10000",
                  "10000",
                  "11111"]

cc.char_5_data = ["01011",
                  "11111",
                  "01011",
                  "10111",
                  "01000",
                  "01110",
                  "10001",
                  "01110"]

cc.char_6_data = ["01001",
"01001",
"10101",
"10101",
"00000",
"10000",
"10000",
"11111"]

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
    str = '     00052                Haengsin  '

    display.lcd_display_extended_string('17:18|{0x04}{0x05}|KTX-{0x02}{0x03}|', 1)

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