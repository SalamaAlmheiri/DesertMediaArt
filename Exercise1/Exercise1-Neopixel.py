# Exercise 1: RGB Neopixel color sequence
# Salama Almheiri
# 11 September 2022

# From: https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/circuitpython-internal-rgb-led
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Internal RGB LED red, green, blue example"""
import time
import board

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1) #1= number of neopixels

led.brightness = 0.6

# Warm to cool color sequence: yellow, orange, red, pink, purple, blue, turquise, green...loop
while True:
    #Yellow
    led[0] = (255, 255, 153)
    time.sleep(0.3)
    led[0] = (255, 255, 0)
    time.sleep(0.3)
    #Orange
    led[0] = (255, 240, 0)
    time.sleep(0.3)
    led[0] = (255, 150, 0)
    time.sleep(0.3)
    led[0] = (255, 110, 0)
    time.sleep(0.3)
    led[0] = (255, 40, 0)
    time.sleep(0.3)
    #Red
    led[0] = (255, 0, 0)
    time.sleep(0.3)
    led[0] = (255, 0, 60)
    time.sleep(0.3)
    led[0] = (255, 0, 127)
    time.sleep(0.3)
    led[0] = (255, 51, 127)
    time.sleep(0.3)
    led[0] = (255, 102, 170)
    time.sleep(0.3)
    #Pink
    led[0] = (255, 0, 255)
    time.sleep(0.3)
    led[0] = (180, 0, 195)
    time.sleep(0.3)
    led[0] = (153, 0, 153)
    time.sleep(0.3)
    #Purple
    led[0] = (153, 51, 255)
    time.sleep(0.3)
    led[0] = (120, 20, 220)
    time.sleep(0.3)
    led[0] = (102, 0, 204)
    time.sleep(0.3)
    #Blue
    led[0] = (50, 0, 204)
    time.sleep(0.3)
    led[0] = (0, 0, 204)
    time.sleep(0.3)
    led[0] = (25, 25, 220)
    time.sleep(0.3)
    led[0] = (51, 51, 255)
    time.sleep(0.3)
    led[0] = (26, 100, 255)
    time.sleep(0.3)
    led[0] = (0, 128, 255)
    time.sleep(0.3)
    led[0] = (0, 180, 227)
    time.sleep(0.3)
    led[0] = (0, 204, 204)
    time.sleep(0.3)
    #Turquise
    led[0] = (50, 226, 195)
    time.sleep(0.3)
    led[0] = (102, 255, 178)
    time.sleep(0.3)
    #Green
    led[0] = (51, 255, 51)
    time.sleep(0.3)
    led[0] = (100, 255, 70)
    time.sleep(0.3)
    led[0] = (178, 255, 102)
    time.sleep(0.3)


