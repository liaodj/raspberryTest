#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO
import time

# 定义单个数码管各段led对应的GPIO口
LED_A = 26
LED_B = 19
LED_C = 13
LED_D = 6
LED_E = 5
LED_F = 11
LED_G = 9
LED_DP = 10

led_list = [LED_A,LED_B,LED_C,LED_D,LED_E,LED_F,LED_G,LED_DP]


# 定义1到4号数码管阳极对应的GPIO口
DIGIT1 = 12
DIGIT2 = 16
DIGIT3 = 20
DIGIT4 = 21

dig_list = [DIGIT1,DIGIT2,DIGIT3,DIGIT4]
# 定义按钮输入的GPIO口
btn = 27

RPi.GPIO.setmode(RPi.GPIO.BCM)

RPi.GPIO.setup(led_list,RPi.GPIO.OUT)
RPi.GPIO.setup(dig_list, RPi.GPIO.OUT)
RPi.GPIO.output(dig_list,True)

RPi.GPIO.setup(btn, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)

# 指定no(1-4)号数码管显示数字num(0-9)，第三个参数是显示不显示小数点（true/false）
def showDigit(no, num, showDotPoint):
    # 先将正极拉低，关掉显示
    RPi.GPIO.output(dig_list, False)
    
    if (num == 0) :
        RPi.GPIO.output(led_list,(False, False, False, False, False, False, True, not showDotPoint))
    elif (num == 1) :
        RPi.GPIO.output(led_list,(True, False, False, True, True, True, True, not showDotPoint))
    elif (num == 2) :
        RPi.GPIO.output(led_list,(False, False, True, False, False, True, False, not showDotPoint))
    elif (num == 3) :
        RPi.GPIO.output(led_list,(False, False, False, False, True, True, False, not showDotPoint))
    elif (num == 4) :
        RPi.GPIO.output(led_list,(True, False, False, True, True, False, False, not showDotPoint))
    elif (num == 5) :
        RPi.GPIO.output(led_list,(False, True, False, False, True, False, False, not showDotPoint))
    elif (num == 6) :
        RPi.GPIO.output(led_list,(False, True, False, False, False, False, False, not showDotPoint))
    elif (num == 7) :
        RPi.GPIO.output(led_list,(False, False, False, True, True, True, True, not showDotPoint))
    elif (num == 8) :
        RPi.GPIO.output(led_list,(False, False, False, False, False, False, False, not showDotPoint))
    elif (num == 9) :
        RPi.GPIO.output(led_list,(False, False, False, False, True, False, False, not showDotPoint))
    
    if (no == 1) :
        RPi.GPIO.output(DIGIT1, True)
    elif (no == 2) :
        RPi.GPIO.output(DIGIT2, True)
    elif (no == 3) :
        RPi.GPIO.output(DIGIT3, True)
    elif (no == 4) :
        RPi.GPIO.output(DIGIT4, True)

try:
    t=0.005
    while True:
        # 按钮按下时显示日期，否则显示时间
        # 为了区别左右的数字，让第二个数码管的小数点显示出来
        #（本来应该是一个冒号，我们这个数码管没有，就用小数点代替了）
        if (RPi.GPIO.input(btn) == 1):
            time.sleep(t)
            showDigit(1, int(time.strftime("%H",time.localtime(time.time()))) / 10, False)
            time.sleep(t)
            showDigit(2, int(time.strftime("%H",time.localtime(time.time()))) % 10, True)
            time.sleep(t)
            showDigit(3, int(time.strftime("%M",time.localtime(time.time()))) / 10, False)
            time.sleep(t)
            showDigit(4, int(time.strftime("%M",time.localtime(time.time()))) % 10, False)
        else:
            time.sleep(t)
            showDigit(1, int(time.strftime("%m",time.localtime(time.time()))) / 10, False)
            time.sleep(t)
            showDigit(2, int(time.strftime("%m",time.localtime(time.time()))) % 10, True)
            time.sleep(t)
            showDigit(3, int(time.strftime("%d",time.localtime(time.time()))) / 10, False)
            time.sleep(t)
            showDigit(4, int(time.strftime("%d",time.localtime(time.time()))) % 10, False)
            
except KeyboardInterrupt:
    pass

# 最后清理GPIO口（不做也可以，建议每次程序结束时清理一下，好习惯）
RPi.GPIO.cleanup()

