#!/usr/bin/env python
# -*- coding: utf-8 -*-

import OPi.GPIO as GPIO
from time import sleep          # this lets us have a time delay

led = 1
#print(f"The BOARD pin selected is {led}")

GPIO.setboard(GPIO.H616)        # Orange Pi Zero 2 board
GPIO.setmode(GPIO.BOARD)        # set up BOARD BCM numbering

for led in range(led, 40):
  try:
    print(f"The BOARD pin selected is {led}")
    GPIO.setup(led, GPIO.OUT)       # set pin as an output (LED)
    GPIO.output(led, 1)       # set port/pin value to 1/HIGH/True
    sleep(0.1)
    GPIO.output(led, 0)       # set port/pin value to 0/LOW/False
    sleep(0.1)
    
    GPIO.output(led, 1)       # set port/pin value to 1/HIGH/True
    sleep(0.1)
    GPIO.output(led, 0)       # set port/pin value to 0/LOW/False
    sleep(0.1)

    sleep(0.5)
    led += 1

  except KeyboardInterrupt:
    GPIO.output(led, 0)           # set port/pin value to 0/LOW/False
    GPIO.cleanup()              # Clean GPIO
    print ("Bye.")

  except:
    print("NOT USABLE")
    led += 1
    pass
