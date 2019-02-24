from adafruit_circuitplayground.express import cpx
import time

RED = (255, 0, 0)   # 255 Red, 0 Green, 0 Blue
GREEN = (0, 255, 0) # 0 Red, 255 Green, 0 Blue
BLUE = (0, 0, 255)  # 0 Red, 0 Green, 255 Blue

cpx.pixels.brightness = 0.1

my_colors = [("Red", RED), ("Green", GREEN), ("Blue", BLUE)]
color_pos = 0

while True: # Keep looping forever...
    name, color = my_colors[color_pos]
    cpx.pixels.fill(color)

    if cpx.button_a or cpx.button_b: # Button A or B was pressed
        color_pos = (color_pos + 1) % len(my_colors)
        next_name, _ = my_colors[color_pos]
        print("Changing color from %s to %s" % (name, next_name))
        time.sleep(0.2)  # Sleep, to make the button less sensitive