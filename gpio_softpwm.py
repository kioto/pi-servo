#/usr/bin/env python3
# -*- coding:utf-8 -*-

#
# RPi.GPIOのソフトウェアPWMを使用したサーボモーターのサンプル
#

import RPi.GPIO as GPIO
import time

PIN = 18

class Servo(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN, GPIO.OUT)
        self._servo = GPIO.PWM(PIN, 50)
        self._servo.start(0)

    def __del__(self):
        self._servo.stop()
        GPIO.cleanup()

    def rotate_left_right(self):
        # Left high
        self._servo.ChangeDutyCycle(12)
        time.sleep(1)
        # Left low
        self._servo.ChangeDutyCycle(7.5)
        time.sleep(1)
        # Right high
        self._servo.ChangeDutyCycle(2.5)
        time.sleep(1)
        # Right low
        self._servo.ChangeDutyCycle(6.5)
        time.sleep(1)


if __name__ == '__main__':
    servo = Servo()
    servo.rotate_left_right()

