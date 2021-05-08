import numpy as np
import pygame as pg


class MAIN:

    def __init__(self, grid_size, grid_count):

        self.grid_size = grid_size
        self.grid_count = grid_count
        self.screen_size = self.grid_size * self.grid_count
        self.radius = (grid_size / 2) - 3
        self.coordinates = [i * self.grid_size + grid_size / 2 for i in range(0, grid_count)]

        self.blue = (20, 20, 200)
        self.black = (10, 10, 10)
        self.yellow = (255, 230, 60)
        self.red = (235, 30, 15)

        self.turn = 1
        self.board = np.zeros((6, 7), dtype=np.int8)

    def turn_color_switch(self):
        if self.turn == 1:
            self.turn = 2
            return self.yellow
        else:
            self.turn = 1
            return self.red

    def pixel_position(self, x, y):
        return y * self.grid_size + self.grid_size / 2, (x+1) * self.grid_size + self.grid_size / 2

    def valid_position(self, col):
        valid = np.where(self.board.T[col] == 0)[0]
        if valid.size > 0:
            return valid[-1]
        else:
            print("full")

    def play_turn(self, surface, col):
        row = self.valid_position(col)
        if not row is None:
            self.board[row, col] = self.turn
            pg.draw.circle(surface=surface,
                           center=self.pixel_position(row, col),
                           color=self.turn_color_switch(),
                           radius=self.radius)

    def horizontal_check(self, col):
        pass
