# imports
from collections import defaultdict
from queue import Queue
from enum import Enum
import time

# writing
NO_SPACES = 2
LETTER_WIDTH = 5
WRITING_TEST = 'abcdefghijklmnopqrstuvwxyz!"#$%&'
WRITING_TEST += "' ()*+,-./:;<=>?@[\]^_`{|}~123456789"

# time specs
DELAY = 0.1

# matrix specs
NO_ROWS = 8 
NO_COLUMNS = 110
NO_LEDS = NO_ROWS * NO_COLUMNS

# led configs
LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# colours
class Colours(Enum):
    Black = 0
    Red = 1
    Green = 2
    Blue = 3
    Yellow = 4
    Orange = 5
    Purple = 6
    Pink = 7

# processes
class Processes(Enum):
    Nothing = 0
    Writing = 1
    Tetris = 2
    Pong = 3
    Watch = 4

# matrix state
class State:
    def __init__(self):
        self.board = [ [Colours.Black for _ in range(NO_COLUMNS)] for _ in range(NO_ROWS)]
        self.current_process = Processes.Nothing
        self.instructions = Queue()
        self.current_instruction = ""
        self.instruction_index = 0
