#/usr/bin/env python3
# -*- coding:utf-8 -*-

#
# wiringpiのソフトウェアPWMを使用したサーボモーターのサンプル
#

import wiringpi

PIN = 18

class Servo(object):
    def __init__(self):
        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(PIN, wiringpi.GPIO.PWM_OUTPUT)
        wiringpi.softPwmCreate(PIN, 0, 100)

    def __del__(self):
        wiringpi.softPwmStop(PIN)

    def rotate_left_right(self):
        # Left high
        wiringpi.softPwmWrite(PIN, 25)
        wiringpi.delay(1000)
        # Left low
        wiringpi.softPwmWrite(PIN, 16)
        wiringpi.delay(1000)
        # Right high
        wiringpi.softPwmWrite(PIN,  5)
        wiringpi.delay(1000)
        # Right low
        wiringpi.softPwmWrite(PIN, 13)
        wiringpi.delay(1000)


if __name__ == '__main__':
    servo = Servo()
    servo.rotate_left_right()

