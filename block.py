import pygame
from colors import Colors
from position import Position

class Block:
    '''
    Parent class for different Tetrimino blocks (children)
    '''
    def __init__(self, id):
        pass

    def move(self, rows, columns):
        pass

    def get_cell_positions(self):
        pass

    def rotate(self):
        pass
    
    def undo_rotate(self):
        pass

    def draw(self, screen, offset_x, offset_y):
        pass