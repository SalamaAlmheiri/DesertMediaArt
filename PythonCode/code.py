# Basic example of blinking LED (+time)
# Salama Almheiri
# 7 September 2022

print('LED Blink')

# built in libraries:
import board
import digitalio #access to pins
import time

print("It is now"+ str(time.monotonic()))
#print('Basic LED is attatched to pin'+ board.LED)

# The variable gives us access to the hardware pin
led = digitalio.DigitalInOut(board.LED)

# set the LED pin as an output so we can turn it on/off
led.direction = digitalio.Direction.OUTPUT

# records the starting time
startTime= time.monotonic()
# how long to blink (5 seconds)
secondsToBlink= 5

print("Starting to blink!")
#while True:  #infinity loop
while (time.monotonic()-startTime)< secondsToBlink:
    led.value = True
    time.sleep(0.5/2)
    led.value = False
    time.sleep(0.5/2)
    print("timeime - %.1f" % time.monotonic())

print("All done!")
