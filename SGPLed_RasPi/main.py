# MacBook Example

# imports
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

def shift():
    for row in range(NO_ROWS):
        for col in range(1, NO_COLUMNS):
            current_state.board[row][col - 1] = current_state.board[row][col]

    for row in range(0, NO_ROWS):
        current_state.board[row][NO_COLUMNS - 1] = Colours.Black

def show():
    for row in range(NO_ROWS):
        print("[ ", end = "")
        for col in range(NO_COLUMNS):
            print(current_state.board[row][col].value, end = " ")

        print("]")
    print('')

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

            # light up led
            if int_string == None:
                current_state.instruction_index = len(current_state.current_instruction)
                break

            current_state.board[int(int_string)][NO_COLUMNS - 1] = Colours.Red

def render():
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

