from sudoku_cell import Cell
import pygame


class Board:
    line_color = (0, 0, 0)
    line_width = 5

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

    def draw(self):
        # draw main horizontal lines
        self.height = self.height - 100
        for i in range(0, 4):
            pygame.draw.line(self.screen, Board.line_color, (0, i * (self.height / 3)),
                             (self.width, i * (self.height / 3)), Board.line_width)
        # draw main vertical lines
        for i in range(1, 3):
            pygame.draw.line(self.screen, Board.line_color, (i * (self.width / 3), 0),
                             (i * (self.width / 3), self.height), Board.line_width)

        # draw horizontal lines for cells
        for i in range(1, 9):
            pygame.draw.line(self.screen, Board.line_color, (0, i * (self.height / 9)),
                             (self.width, i * (self.height / 9)), 2)
        # draw vertical lines for cells
        for i in range(1, 9):
            pygame.draw.line(self.screen, Board.line_color, (i * (self.width / 9), 0),
                             (i * (self.width / 9), self.height), 2)
        self.height = self.height + 100

    def select(self, row, col):
        pass

    def click(self, x, y):
        pass

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass
