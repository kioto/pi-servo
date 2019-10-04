#/usr/bin/env python3
# -*- coding:utf-8 -*-

#
# wiringpiのsoftServoを使用したサーボモーターのサンプル
#

import wiringpi

PIN = 18

class Servo(object):
    def __init__(self):
        wiringpi.wiringPiSetupGpio()
        wiringpi.softServoSetup(PIN,-1,-1,-1,-1,-1,-1,-1)

    def rotate_left_right(self):
        # Left high
        wiringpi.softServoWrite(PIN, 1000)
        wiringpi.delay(1000)
        # Left low
        wiringpi.softServoWrite(PIN, 600)
        wiringpi.delay(1000)
        # Right high
        wiringpi.softServoWrite(PIN, 0)
        wiringpi.delay(1000)
        # Right high
        wiringpi.softServoWrite(PIN, 300)
        wiringpi.delay(1000)

if __name__ == '__main__':
    servo = Servo()
    servo.rotate_left_right()

