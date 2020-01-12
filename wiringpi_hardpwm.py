#/usr/bin/env python3
# -*- coding:utf-8 -*-

#
# wiringpiのハードウェアPWMを使用したサーボモーターのサンプル
#

import wiringpi

PIN = 18

class Servo(object):
    def __init__(self):
        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(PIN, wiringpi.GPIO.PWM_OUTPUT)
        wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
        # Duty Cycle=100%の時に1024
        wiringpi.pwmSetRange(1024)
        # PWM周波数
        # PWMコントローラの動作クロック周波数19.2MHz / PWM信号の周波数50Hz
        #   x レンジ1024= 393
        wiringpi.pwmSetClock(393)

    def rotate_left_right(self):
        # Left hight
        wiringpi.pwmWrite(PIN, 123) # +90deg. (1024 x 12%)
        wiringpi.delay(1000)
        # Left low
        wiringpi.pwmWrite(PIN, 80) # +90deg. (1024 x 9.0%)
        wiringpi.delay(1000)
        # Right
        wiringpi.pwmWrite(PIN, 26) # -90deg. (1024 x 2.5%)
        wiringpi.delay(1000)
        # Left low
        wiringpi.pwmWrite(PIN, 65) # +90deg. (1024 x 6.3%)
        wiringpi.delay(1000)
        # Stop
        # ハードウェアPWMはこれがないと止まらない。
        wiringpi.pwmWrite(PIN, 74) # 0deg. (1024 x 7.25%)

        print('done')
        

if __name__ == '__main__':
    servo = Servo()
    servo.rotate_left_right()
