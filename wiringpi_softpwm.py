#/usr/bin/env python3
# -*- coding:utf-8 -*-

#
# wiringpiのソフトウェアPWMを使用したサーボモーターのサンプル
#

import wiringpi

PIN = 18

def initialize():
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(PIN, wiringpi.GPIO.PWM_OUTPUT)
    wiringpi.softPwmCreate(PIN, 0, 100)

def rotate_left_right():
    # Left
    wiringpi.softPwmWrite(PIN, 25)
    wiringpi.delay(1000)
    # Right
    wiringpi.softPwmWrite(PIN,  5)
    wiringpi.delay(1000)


if __name__ == '__main__':
    initialize()
    rotate_left_right()
    print('done')

# end of file

