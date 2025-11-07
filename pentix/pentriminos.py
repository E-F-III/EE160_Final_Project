from base_tetris.block import Block
from base_tetris.position import Position

class I_block(Block):
    def __init__(self):
        super().__init__(id = 1)

        self.cells = {
            0:[Position(3,0),Position(3,1),Position(3,2),Position(3,3),Position(3,4),],
            1:[Position(),Position(),Position(),Position(),Position(),],
            2:[Position(),Position(),Position(),Position(),Position(),],
            3:[Position(),Position(),Position(),Position(),Position(),],
        }

        self.move(0, 3)