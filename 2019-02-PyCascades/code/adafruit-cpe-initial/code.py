# This is forked version of the original demo optimized for the VS Code Circuit Playground Express add-in

import time
import random
from adafruit_circuitplayground.express import cpx

# Set this to False to turn on off the capacitive touch tones
TOUCH_PIANO = True

# NeoPixel color names
WHITE = (50, 50, 50)
DARKORANGE = (80, 44, 0)
ORANGE = (244, 117, 33)
YELLOWORANGE = (216, 59, 1)
OFF = (0, 0, 0)

# Dim the lights a bit, they're bright
cpx.pixels.brightness = 0.3

# Play startup noise on boot
cpx.play_file("Fanfare.wav")


def wheel(pos):
    # Return color value for position
    if (pos < 0) or (pos > 255):
        return (0, 0, 0)
    if pos < 85:
        return ORANGE
    elif pos < 170:
        pos -= 85
        return YELLOWORANGE
    else:
        pos -= 170
    return WHITE


# Lights on or off
lights_on = True
# LED on or off
led_on = False
# Counter for all 10 pixels
pixeln = 0
# Can tell the switch changed
last_switch = cpx.switch


while True:
    # LIGHTS
    # This  makes a swirling pattern of orange colors!
    if lights_on:
        for p in range(10):
            color = wheel(25 * ((pixeln + p) % 10))
            cpx.pixels[p] = [int(c * ((10 - (pixeln + p) % 10)) / 10.0) for c in color]

        # Each time 'round we tick off one pixel at a time
        if cpx.switch:  # depending on the switch we'll go clockwise
            pixeln += 1
            if pixeln > 9:
                pixeln = 0
        else:  # or counter clockwise, flip the switch to change direction
            pixeln -= 1
            if pixeln < 0:
                pixeln = 9

        # BUTTONS
        # Press and hold to make the lights dimmer or brighter
        # Dimmer
        if cpx.button_a:
            print("Button A pressed")
            cpx.pixels.brightness = 0.1
        # Brighter!
        if cpx.button_b:
            print("Button B pressed")
            cpx.pixels.brightness = 0.5
        # Neither buttons pressed
        if not cpx.button_a and not cpx.button_b:
            cpx.pixels.brightness = 0.3

    # SWITCH
    # Check the switch
    if cpx.switch:
        if last_switch != cpx.switch:  # if it moved, print it out
            print("Switch moved left")
    else:
        if last_switch != cpx.switch:
            print("Switch moved right")
    last_switch = cpx.switch

    # CAPACITIVE TOUCH
    # Touch A1 - A7 on the device to play music
    if TOUCH_PIANO:
        if cpx.touch_A4:
            cpx.play_tone(524, 0.25)
        elif cpx.touch_A5:
            cpx.play_tone(588, 0.25)
        elif cpx.touch_A6:
            cpx.play_tone(660, 0.25)
        elif cpx.touch_A7:
            cpx.play_tone(698, 0.25)
        elif cpx.touch_A1:
            cpx.play_tone(784, 0.25)
        elif cpx.touch_A2:
            cpx.play_tone(784, 0.25)
        elif cpx.touch_A3:
            cpx.play_tone(988, 0.25)

    # SENSORS
    # When the device is running use the command "Device Simulator Express: Open Serial Monitor" to get read outs from the device
    if pixeln == 0:  # Pprint sensor data every time the lights go around
        print("Temperature: %0.1f *C" % cpx.temperature)
        print("Light Level: %d" % cpx.light)
        x, y, z = cpx.acceleration
        print("Accelerometer: (%0.1f, %0.1f, %0.1f) m/s^2" % (x, y, z))
        print("-" * 40)

    # SHAKE
    if cpx.shake(shake_threshold=20):  # Look for a shake
        cpx.pixels.fill(OFF)  # Turn off lights and pause sensor reporting
        lights_on = not lights_on  # Switch light bool
        led_on = not led_on  # Switch LED bool

    # LED
    cpx.red_led = led_on  # Turns on and off the little LED next to USB on

    # loop to the beginning!
