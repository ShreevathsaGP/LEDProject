# imports
from collections import defaultdict
from queue import Queue
from enum import Enum

from globy import *

# writer class
class Writer:
    # constructor
    def __init__(self, in_state):
        # useful
        self.current_state = in_state
        self.letter_map = defaultdict(str)

        # others
        self.sample_string = ""
        self.letter_width = LETTER_WIDTH
        self.temp = 0
        self.top = 0
        self.bottom = 0

        # initialize letter map
        self.init_mappings()

    # write given string
    def write(self, in_string):
        # reset board
        self.current_state.current_process = Processes.Writing
        for row in range(NO_ROWS):
            for col in range(NO_COLUMNS):
                self.current_state.board[row][col] = Colours.Black

        # letter wise instructions
        for char in in_string:
            self.current_state.instructions.put(self.letter_map[char.lower()])


    # add no spaces to string
    def add_space(self, no, in_string):
        for _ in range(no):
            in_string += ' '
            in_string += '|'

        return in_string

    # initialize letter-mappings
    def init_mappings(self):
        if self.letter_width <= 3: return False # board not wide enough
        if NO_ROWS <= 4: return False # board not long enough

        # [ ] (Space) 
        self.sample_string = ""
        self.sample_string += ' |'
        self.sample_string += ' |'
        self.sample_string += ' |'
        self.letter_map[' '] = self.sample_string

        # A
        self.sample_string = ""
        for i in range(2, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(0, self.letter_width - 2):
            self.sample_string += '1|'
            self.sample_string += str(NO_ROWS // 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        for i in range(2, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map['a'] = self.sample_string

        # B
        self.sample_string = ""
        for i in range(1, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(0, self.letter_width - 2):
            self.sample_string += "1|"
            self.sample_string += str(NO_ROWS // 2)
            self.sample_string += '|'
            self.sample_string += str(NO_ROWS - 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        for i in range(2, NO_ROWS - 2):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map['b'] = self.sample_string

        # C
        self.sample_string = ""
        for i in range(2, NO_ROWS - 2):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(self.letter_width - 1):
            self.sample_string += '1|'
            self.sample_string += str(NO_ROWS - 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string = self.add_space(NO_SPACES - 1, self.sample_string)
        self.letter_map['c'] = self.sample_string
        
        # D
        self.sample_string = ""
        for i in range(1, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(self.letter_width - 2):
            self.sample_string += '1|'
            self.sample_string += str(NO_ROWS - 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        for i in range(2, NO_ROWS - 2):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map['d'] = self.sample_string

        # E
        self.sample_string = ""
        for i in range(1, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(self.letter_width - 1):
            self.sample_string += '1|'
            self.sample_string += str(NO_ROWS // 2)
            self.sample_string += '|'
            self.sample_string += str(NO_ROWS - 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string = self.add_space(NO_SPACES - 1, self.sample_string)
        self.letter_map['e'] = self.sample_string

        # F
        self.sample_string = ""
        for i in range(1, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(self.letter_width - 1):
            self.sample_string += '1|'
            self.sample_string += str(NO_ROWS // 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string = self.add_space(NO_SPACES - 1, self.sample_string)
        self.letter_map['f'] = self.sample_string

        # G
        self.sample_string = ""
        for i in range(1, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range((self.letter_width // 2) - 1):
            self.sample_string += '1|'
            self.sample_string += str(NO_ROWS - 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        for i in range(self.letter_width - ((self.letter_width // 2) - 1) - 2):
            self.sample_string += '1|'
            self.sample_string += str(NO_ROWS // 2)
            self.sample_string += '|'
            self.sample_string += str(NO_ROWS - 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string += '1|'
        self.sample_string += str(NO_ROWS // 2)
        self.sample_string += '|'
        for i in range((NO_ROWS // 2) + 1, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map['g'] = self.sample_string

        # H
        self.sample_string = ""
        for i in range(1, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(self.letter_width - 2):
            self.sample_string += str(NO_ROWS // 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        for i in range(1, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map['h'] = self.sample_string

        # I
        self.sample_string = ""
        for i in range((self.letter_width - 1) // 2):
            self.sample_string += '1|'
            self.sample_string += str(NO_ROWS - 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        for i in range(1, NO_ROWS - 1):
            self.sample_string += str(i) 
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range((self.letter_width - 1) - ((self.letter_width - 1) // 2)):
            self.sample_string += '1|'
            self.sample_string += str(NO_ROWS - 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string = self.add_space(NO_SPACES - 1, self.sample_string)
        self.letter_map['i'] = self.sample_string

        # J
        self.sample_string = ""
        for i in range((self.letter_width - 1) // 2):
            self.sample_string += '1|'
            self.sample_string += str(NO_ROWS - 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        for i in range(1, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range((self.letter_width - 1) - ((self.letter_width - 1) // 2)):
            self.sample_string += '1|'
            self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string = self.add_space(NO_SPACES - 1, self.sample_string)
        self.letter_map['j'] = self.sample_string

        # K
        self.sample_string = ""
        for i in range(1, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(self.letter_width - 3):
            self.sample_string += str(NO_ROWS // 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string += str((NO_ROWS // 2) - 1)
        self.sample_string += '|'
        self.sample_string += str((NO_ROWS // 2) + 1)
        self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(1, NO_ROWS - 1):
            if ((NO_ROWS // 2) - 2) < i < ((NO_ROWS // 2) + 2):
                continue
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map['k'] = self.sample_string

        # L
        self.sample_string = ""
        for i in range(1, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(self.letter_width - 1):
            self.sample_string += str(NO_ROWS - 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string = self.add_space(NO_SPACES - 1, self.sample_string)
        self.letter_map['l'] = self.sample_string

        # M
        self.sample_string = ""
        for i in range(2, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range((self.letter_width - 3) // 2):
            self.sample_string += '1|'
            self.sample_string = self.add_space(1, self.sample_string)
        for i in range(2, (NO_ROWS // 2) + 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range((self.letter_width - 3) - ((self.letter_width - 3) // 2)):
            self.sample_string += '1|'
            self.sample_string = self.add_space(1, self.sample_string)
        for i in range(2, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map['m'] = self.sample_string

        # N
        self.sample_string = ""
        self.temp = 2
        for i in range(1, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(self.letter_width - 2):
            self.sample_string += str(self.temp)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
            self.temp += 1 if self.temp < NO_ROWS - 2 else 0
        for i in range(1, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map['n'] = self.sample_string


        # O
        self.sample_string = ""
        for i in range(2, NO_ROWS - 2):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(self.letter_width - 2):
            self.sample_string += '1|'
            self.sample_string += str(NO_ROWS - 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        for i in range(2, NO_ROWS - 2):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map['o'] = self.sample_string

        # P
        self.sample_string = ""
        for i in range(1, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(self.letter_width - 2):
            self.sample_string += '1|'
            self.sample_string += str(NO_ROWS // 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        for i in range(2, NO_ROWS // 2):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map['p'] = self.sample_string

        # Q
        self.sample_string = ""
        for i in range(2, NO_ROWS - 2):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(self.letter_width - 3):
            self.sample_string += '1|'
            self.sample_string += str(NO_ROWS - 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string += '1|'
        self.sample_string += str(NO_ROWS - 3)
        self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(2, NO_ROWS - 1):
            if i == (NO_ROWS - 3):
                continue
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map['q'] = self.sample_string

        # R
        self.sample_string = ""
        for i in range(1, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(self.letter_width - 2):
            self.sample_string += '1|'
            self.sample_string += str(NO_ROWS // 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        for i in range(2, NO_ROWS - 1):
            if i == (NO_ROWS // 2):
                continue
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map['r'] = self.sample_string

        # S
        self.sample_string = ""
        for i in range(2, NO_ROWS // 2):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string += str(NO_ROWS - 2)
        self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(self.letter_width - 2):
            self.sample_string += '1|'
            self.sample_string += str(NO_ROWS // 2)
            self.sample_string += '|'
            self.sample_string += str(NO_ROWS - 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string += '1|'
        for i in range((NO_ROWS // 2) + 1, NO_ROWS - 2):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map['s'] = self.sample_string

        # T
        self.sample_string = ""
        for i in range((self.letter_width - 1) // 2):
            self.sample_string += '1|'
            self.sample_string = self.add_space(1, self.sample_string)
        for i in range(1, NO_ROWS - 1):
            self.sample_string += str(i) 
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range((self.letter_width - 1) - ((self.letter_width - 1) // 2)):
            self.sample_string += '1|'
            self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string = self.add_space(NO_SPACES - 1, self.sample_string)
        self.letter_map['t'] = self.sample_string

        # U
        self.sample_string = ""
        for i in range(1, NO_ROWS - 2):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(self.letter_width - 2):
            self.sample_string += str(NO_ROWS - 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        for i in range(1, NO_ROWS - 2):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map['u'] = self.sample_string
        
        # V
        self.sample_string = ""
        for i in range(1, NO_ROWS - 3):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string += str(NO_ROWS - 3)
        self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(self.letter_width - 4):
            self.sample_string += str(NO_ROWS - 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string += str(NO_ROWS - 3)
        self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(1, NO_ROWS - 3):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map['v'] = self.sample_string

        # W
        self.sample_string = ""
        for i in range(1, NO_ROWS - 2):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range((self.letter_width - 3) // 2):
            self.sample_string += str(NO_ROWS - 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        for i in range((NO_ROWS // 2), NO_ROWS - 2):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range((self.letter_width - 3) - ((self.letter_width - 3) // 2)):
            self.sample_string += str(NO_ROWS - 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        for i in range(1, NO_ROWS - 2):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map['w'] = self.sample_string

        # X
        self.sample_string = ""
        for i in range(1, NO_ROWS - 1):
            if (NO_ROWS // 2) - 2 < i < (NO_ROWS // 2) + 2:
                continue
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string += str((NO_ROWS // 2) - 1)
        self.sample_string += '|'
        self.sample_string += str((NO_ROWS // 2) + 1)
        self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(self.letter_width - 4):
            self.sample_string += str(NO_ROWS // 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string += str((NO_ROWS // 2) - 1)
        self.sample_string += '|'
        self.sample_string += str((NO_ROWS // 2) + 1)
        self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(1, NO_ROWS - 1):
            if (NO_ROWS // 2) - 2 < i < (NO_ROWS // 2) + 2:
                continue
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map['x'] = self.sample_string


        # Y
        self.sample_string = ""
        for i in range(1, NO_ROWS // 2):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range((self.letter_width - 3) // 2):
            self.sample_string += str(NO_ROWS // 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        for i in range(NO_ROWS // 2, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range((self.letter_width - 3) - ((self.letter_width - 3) // 2)):
            self.sample_string += str(NO_ROWS // 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        for i in range(1, NO_ROWS // 2):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map['y'] = self.sample_string

        # Z
        self.letter_map['z'] = self.letter_map['s']

        # !
        self.sample_string = ""
        for i in range(1, NO_ROWS - 1):
            if i == NO_ROWS - 3:
                continue
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map['!'] = self.sample_string

        # '
        self.sample_string = ""
        for i in range(1, (NO_ROWS // 4) + 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map["'"] = self.sample_string

        # "
        self.letter_map['"'] = self.letter_map["'"]

        # (
        self.sample_string = ""
        for i in range(1, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string += '0|'
        self.sample_string += str(NO_ROWS - 1)
        self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map["("] = self.sample_string

        # )
        self.sample_string = ""
        self.sample_string += '0|'
        self.sample_string += str(NO_ROWS - 1)
        self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(1, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map[")"] = self.sample_string

        # *
        self.sample_string = ""
        no_done = 0
        for _ in range(2):
            for i in range(1, (NO_ROWS // 4) + 1):
                self.sample_string += str(i)
                self.sample_string += '|'
                no_done += 1
            self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string = self.add_space(NO_SPACES - 1, self.sample_string)
        self.letter_map['*'] = self.sample_string

        # +
        self.sample_string = ""
        for i in range((self.letter_width - 1) // 2):
            self.sample_string += str(NO_ROWS // 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        for i in range(1, NO_ROWS - 1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range((self.letter_width - 1) - ((self.letter_width - 1) // 2)):
            self.sample_string += str(NO_ROWS // 2)
            self.sample_string += '|'
            self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string = self.add_space(NO_SPACES - 1, self.sample_string)
        self.letter_map["+"] = self.sample_string

        # ,
        self.sample_string = ""
        self.sample_string += str(NO_ROWS - 2)
        self.sample_string += '|' 
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(NO_ROWS - 3, (NO_ROWS - (NO_ROWS // 4)) - 2, -1):
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map[","] = self.sample_string

        # -
        self.sample_string = ""
        for i in range(self.letter_width - 1):
            self.sample_string += f"{NO_ROWS // 2}|"
            self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string = self.add_space(NO_SPACES - 1, self.sample_string)
        self.letter_map["-"] = self.sample_string

        # .
        self.sample_string = ""
        self.sample_string = str(NO_ROWS - 2)
        self.sample_string += '|' 
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map["."] = self.sample_string

        # :
        self.sample_string = ""
        self.sample_string += f"{(NO_ROWS // 2) - 1}|"
        self.sample_string += f"{(NO_ROWS // 2) + 1}|"
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map[":"] = self.sample_string
        
        # ;
        self.sample_string = ""
        self.sample_string += f"{(NO_ROWS // 2) - 1}|"
        self.sample_string += f"{(NO_ROWS // 2) + 1}|"
        self.sample_string += f"{(NO_ROWS // 2) + 2}|"
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map[";"] = self.sample_string

        # =
        self.sample_string = ""
        for i in range(self.letter_width):
            self.sample_string += f"{(NO_ROWS // 2) - 1}|"
            self.sample_string += f"{(NO_ROWS // 2) + 1}|"
            self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string = self.add_space(NO_SPACES - 1, self.sample_string)
        self.letter_map["="] = self.sample_string

        # [
        self.sample_string = ""
        for i in range(0, NO_ROWS):
            self.sample_string += str(i)
            self.sample_string += "|"
        self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string += "0|"
        self.sample_string += f"{NO_ROWS - 1}|"
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map["["] = self.sample_string

        # ]
        self.sample_string = ""
        self.sample_string += "0|"
        self.sample_string += f"{NO_ROWS - 1}|"
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(0, NO_ROWS):
            self.sample_string += str(i)
            self.sample_string += "|"
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map["]"] = self.sample_string

        # ?
        self.sample_string = ""
        for i in range((self.letter_width - 1) // 2):
            self.sample_string += f"1|"
            self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string += "1|"
        for i in range(NO_ROWS // 2, NO_ROWS - 1):
            if i == NO_ROWS - 3:
                continue
            self.sample_string += str(i)
            self.sample_string += '|'
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range((self.letter_width - 1) - ((self.letter_width - 1) // 2) - 1):
            self.sample_string += f"1|"
            self.sample_string += f"{NO_ROWS // 2}|"
            self.sample_string = self.add_space(1, self.sample_string)
        for i in range(1, (NO_ROWS // 2) + 1):
            self.sample_string += f"{i}|"
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map["?"] = self.sample_string

        # >
        self.sample_string = ""
        for i in range(self.letter_width - 1):
            self.sample_string += f"{(NO_ROWS // 2) - 1}|"
            self.sample_string += f"{(NO_ROWS // 2) + 1}|"
            self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string += f"{NO_ROWS // 2}|"
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map[">"] = self.sample_string

        # <
        self.sample_string = ""
        self.sample_string += f"{NO_ROWS // 2}|"
        self.sample_string = self.add_space(1, self.sample_string)
        for i in range(self.letter_width - 1):
            self.sample_string += f"{(NO_ROWS // 2) - 1}|"
            self.sample_string += f"{(NO_ROWS // 2) + 1}|"
            self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string = self.add_space(NO_SPACES - 1, self.sample_string)
        self.letter_map["<"] = self.sample_string

        # _
        self.sample_string = ""
        for i in range(self.letter_width):
            self.sample_string += f"{NO_ROWS - 2}|"
            self.sample_string = self.add_space(1, self.sample_string)
        self.sample_string = self.add_space(NO_SPACES - 1, self.sample_string)
        self.letter_map["_"] = self.sample_string
        
        # `
        self.letter_map['`'] = self.letter_map["'"]

        # {
        self.letter_map['{'] = self.letter_map['(']

        # |
        self.sample_string = ""
        for i in range(2, NO_ROWS):
            self.sample_string += f"{i}|"
        self.sample_string = self.add_space(NO_SPACES, self.sample_string)
        self.letter_map["|"] = self.sample_string

        # }
        self.letter_map['}'] = self.letter_map[')']

        # 1

        # 2

        # 3

        # 4

        # 5

        # 6

        # 7

        # 8

        # 9

        # @

        # \

        # /

        # ^

        # #

        # $

        # %

        # &

        # ~
