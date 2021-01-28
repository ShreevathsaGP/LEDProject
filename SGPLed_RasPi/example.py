# Raspberry Pi Example

# raspberry pi imports
# from rpi_ws281x import *

# regular imports
from collections import defaultdict
from queue import Queue
from enum import Enum
import time

from glob import *
from writing import Writer

# globals
current_state = State()
writer = Writer(current_state)
current_time = 0
previous_time = time.time()
int_string = ""
running = True
orientation = 0 # 0 = right | 1 = left
actual_index = 0

# initialize strip
# strip = Adafruit_Neopixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# strip.begin()

def shift():
    for row in range(NO_ROWS):
        for col in range(1, NO_COLUMNS):
            current_state.board[row][col - 1] = current_state.board[row][col]

    for row in range(0, NO_ROWS):
        current_state.board[row][NO_COLUMNS - 1] = Colours.Black

def console_show():
    for row in range(NO_ROWS):
        print("[ ", end = "")
        for col in range(NO_COLUMNS):
            print(current_state.board[row][col].value, end = " ")

        print("]")
    print('')

def show():
    actual_index = 0
    orientation = 0 # left
    for row in range(NO_ROWS):
        if orientation == 1:
            # left <-- right
            for col in range(NO_COLUMNS - 1, -1, -1):
                # print(RedChannel[current_state.board[row][col]], GreenChannel[current_state.board[row][col]], BlueChannel[current_state.board[row][col]])
                # strip.setPixelColor(actual_index, Color(RedChannel[current_state.board[row][col]], GreenChannel[current_state.board[row][col]], BlueChannel[current_state.board[row][col]]))
                continue

                actual_index += 1
            orientation = 0 # right
        else:
            # left --> right
            for col in range(0, NO_COLUMNS, 1):
                # print(RedChannel[current_state.board[row][col]], GreenChannel[current_state.board[row][col]], BlueChannel[current_state.board[row][col]])
                # strip.setPixelColor(actual_index, Color(RedChannel[current_state.board[row][col]], GreenChannel[current_state.board[row][col]], BlueChannel[current_state.board[row][col]]))
                continue

                actual_index += 1
            orientation = 1 # left
    # strip.show()

def update():
    if current_state.current_process == Processes.Writing:
        # check instruction update
        if current_state.instruction_index > (len(current_state.current_instruction) - 1):
            if current_state.instructions.empty(): return
            current_state.instruction_index = 0
            current_state.current_instruction = current_state.instructions.get()

        # execute the instructions
        for i in range(current_state.instruction_index, len(current_state.current_instruction)):
            pos = current_state.current_instruction.find('|', current_state.instruction_index)
            int_string = current_state.current_instruction[current_state.instruction_index: pos] if pos != -1 else None
            current_state.instruction_index = pos + 1 if pos != -1 else -1

            # next column
            if int_string == ' ':
                break

            if int_string == None:
                current_state.instruction_index = len(current_state.current_instruction)
                break

            current_state.board[int(int_string)][NO_COLUMNS - 1] = Colours.Red

def render():
    console_show()
    show()

    if current_state.current_process == Processes.Writing:
        shift()

if __name__ == '__main__':
    previous_time = time.time()
    writer.write("happy new year!")
    while True:
        current_time = time.time()
        if current_time - previous_time > DELAY:
            previous_time = current_time
            update()
            render()

