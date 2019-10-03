#/usr/bin/env python3
# -*- coding:utf-8 -*-

#
# wiringpiのsoftServoを使用したサーボモーターのサンプル
#

import wiringpi

PIN = 18

def initialize():
    wiringpi.wiringPiSetupGpio()
    wiringpi.softServoSetup(PIN,-1,-1,-1,-1,-1,-1,-1)

def rotate_left_right():
    # Left
    wiringpi.softServoWrite(PIN, 1000)
    wiringpi.delay(1000)
    # Right
    wiringpi.softServoWrite(PIN, 0)
    wiringpi.delay(1000)

if __name__ == '__main__':
    initialize()
    rotate_left_right()
    print('done')

# end of file

