# imports
from collections import defaultdict
import random
from queue import Queue
from enum import Enum
import keyboard as keyboard_state

from globy import *

# snake class
class Snake:
    # constructor
    def __init__(self, in_state):
        # useful
        self.current_state = in_state
        self.score = 0

        # snake information
        self.snake_colour = SNAKE_COLOUR
        self.snake_dead_colour = SNAKE_DEAD_COLOUR
        self.snake = []
        self.direction = None
        self.length = 0
        self.dead = False

        # apple information
        self.apple_colour = APPLE_COLOUR
        self.apple_position = None

    # start game
    def start(self):
        # reset board
        self.current_state.current_process = Processes.Snake
        for row in range(NO_ROWS):
            for col in range(NO_COLUMNS):
                self.current_state.board[row][col] = Colours.Black
        
        # reset game
        self.snake = [((NO_ROWS // 2), (NO_COLUMNS // 2)),
                ((NO_ROWS // 2) + 1, (NO_COLUMNS // 2)),
                ((NO_ROWS // 2) + 2, (NO_COLUMNS // 2))]
        self.direction = random.choice([Directions.Up, Directions.Down, Directions.Left, Directions.Right])
        self.length = 3
        self.score = 0
        self.apple_position = (3, 3)

        # not dead
        self.dead = False

        # initial render
        self.init_render()

    # stop game
    def stop(self):
        # reset board
        self.current_state.current_process = Processes.Nothing
        for row in range(NO_ROWS):
            for col in range(NO_COLUMNS):
                self.current_state.board[row][col] = Colours.Black

    # key pressed
    def check_keys(self):
        if keyboard_state.is_pressed('w') == 1:
            # up
            # print("w")
            self.direction = Directions.Up
            return
        elif keyboard_state.is_pressed('a') == 1:
            # left
            # print("a")
            self.direction = Directions.Left
            return
        elif keyboard_state.is_pressed('s') == 1:
            # down
            # print("s")
            self.direction = Directions.Down
            return
        elif keyboard_state.is_pressed('d') == 1:
            # right
            # print("d")
            self.direction = Directions.Right
            return
        elif keyboard_state.is_pressed('r') == 1:
            if self.dead:
                # restart game
                self.start()

    # one step in game
    def step(self):
        if self.dead:
            for piece in self.snake[1:]:
                self.current_state.board[piece[0]][piece[1]] = self.snake_dead_colour
            return

        # insert new head
        if self.direction == Directions.Up:
            self.snake.insert(0, ((self.snake[0][0] - 1), (self.snake[0][1])))
        elif self.direction == Directions.Down:
            self.snake.insert(0, ((self.snake[0][0] + 1), (self.snake[0][1])))
        elif self.direction == Directions.Left:
            self.snake.insert(0, ((self.snake[0][0]), (self.snake[0][1] - 1)))
        else:
            self.snake.insert(0, ((self.snake[0][0]), (self.snake[0][1] + 1)))

        # check for death
        if ((self.snake[0][0] < 0) or (self.snake[0][0] > (NO_ROWS - 1)) or ((self.snake[0][1] < 0) or (self.snake[0][1] > (NO_COLUMNS - 1))) or (self.snake[0] in self.snake[1:])):
            self.dead = True
            return

        self.current_state.board[self.snake[0][0]][self.snake[0][1]] = self.snake_colour

        # food
        if self.snake[0] == self.apple_position:
            # self.current_state.board[self.apple_position[0]][self.apple_position[1]] = Colours.Black
            self.apple_position = (random.randint(1, NO_ROWS - 1), random.randint(1, NO_COLUMNS - 1))
            if self.apple_position not in self.snake:
                self.current_state.board[self.apple_position[0]][self.apple_position[1]] = self.apple_colour
        else:
            # remove from board
            tail = self.snake.pop()
            self.current_state.board[tail[0]][tail[1]] = Colours.Black
    
    def init_render(self):
        # render snake
        for piece in self.snake:
            self.current_state.board[piece[0]][piece[1]] = self.snake_colour

        # render apple
        self.current_state.board[self.apple_position[0]][self.apple_position[1]] = self.apple_colour
