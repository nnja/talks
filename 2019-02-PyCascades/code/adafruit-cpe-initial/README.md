Welcome to CircuitPython!
#############################

Visit the Circuit Playground Express (CPX) product page here for more info: 
    https://adafruit.com/product/3333
To get started with CircuitPython, which comes built into your CPX, visit:
    https://learn.adafruit.com/welcome-to-circuitpython

#############################

The Circuit Playground Express (CPX) has a very tiny disk drive so we have 
disabled Mac OS X indexing which could take up that valuable space. 

So *please* do not remove the empty .fseventsd/no_log, .metadata_never_index 
or .Trashes files! 

#############################

The pre-loaded demo shows off some of what your Circuit Playground Express 
can do with CircuitPython:

  * The built in NeoPixels LEDs can show any color, the LEDs will swirl 
    through the rainbow

  * Pad A0 is an analog output, when audio is playing from the speaker you 
    can also see the sine waves on this pad

  * The built in thermistor temperature is printed out on the REPL, you 
    can try breathing on the sensor to make the temperature reading go up

  * The built in light sensor level is printed out on the REPL, shine a 
    light to see the number increase

  * The built in accelerometer motion data is printed out on the REPL, you 
    can try moving the CPX around to make the numbers change

  * There are two buttons, when the left one is pressed the LEDs will be 
    dimmer. When the right one is pressed the LEDs will be brighter.

  * When the CPX is tapped, it will play a video game coin sound or an eep

  * A slide switch determines which way the LEDs swirl, clockwise or counter

For more details on how to use CircuitPython, visit 
    https://adafruit.com/product/3333 
and check out all the tutorials we have!

#############################
CircuitPython Quick Start:

Changing the code is as easy as editing main.py in your favorite text editor. 

Our recommended editor is Mu, which is great for simple projects, and comes
with a built in REPL serial viewer! It is available for Mac, Windows & Linux
  https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor

After the file is saved, CircuitPython will automatically reload the latest 
code. 

  * You can try changing the startup sound by finding the line with
        cpx.play_file("Coin.wav")   # Play a coin sound on boot
    And changing the file name from "Coin.wav" to "Fanfare.wav"

  * Turn the CPX into a little touch-piano! Find this line
        TOUCH_PIANO = False
    And change 'False' to 'True. Now, pads A1 through A7 are capacitive 
    touch inputs. When they are touched, a tone will play from the 
    speaker. The touch pads also come through the back of the board so
    touching the back may trigger sounds.

Connecting to the serial port will give you access to sensor information, 
better error messages and an interactive CircuitPython (known as the REPL). 
On Windows we recommend Mu, Tera Term or PuTTY. 
On Mac OSX and Linux, use Mu or 'screen' can be used from a terminal.
