class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        # setter for this cell's value
        self.value = value

    def set_sketched_value(self, value):
        # setter for this cell's sketched value
        self.value = value

    def draw(self):
        # draws this cell, along with the value inside it
        # if this cell has a nonzero value, that value is displayed
        # otherwise, no value is displayed in the cell
        # the cell is outlined red if it is currently selected
        pass

