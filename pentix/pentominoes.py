from base_tetris.block import Block
from base_tetris.position import Position

class I5_block(Block):
    def __init__(self):
        super().__init__(id = 1)

        self.cells = {
            0:[Position(0,0),Position(0,1),Position(0,2),Position(0,3),Position(0,4),],
            1:[Position(0,2),Position(1,2),Position(2,2),Position(3,2),Position(4,2),],
        }

        self.move(0, 3)

class V5_block(Block):
    def __init__(self):
        super().__init__(id = 2)

        self.cells = {
            0:[Position(0,2),Position(1,2),Position(2,0),Position(2,1),Position(2,2),],
            1:[Position(0,0),Position(1,0),Position(2,0),Position(2,1),Position(2,2),],
            2:[Position(0,0),Position(0,1),Position(0,2),Position(1,0),Position(2,0),],
            3:[Position(0,0),Position(0,1),Position(0,2),Position(1,2),Position(2,2),],
        }

        self.move(0, 3)

class T5_block(Block):
    def __init__(self):
        super().__init__(id = 3)

        self.cells = {
            0:[Position(0,0),Position(0,1),Position(0,2),Position(1,1),Position(2,1),],
            1:[Position(1,0),Position(1,1),Position(1,2),Position(0,2),Position(2,2),],
            2:[Position(0,1),Position(1,1),Position(2,0),Position(2,1),Position(2,2),],
            3:[Position(0,0),Position(1,0),Position(2,0),Position(1,1),Position(1,2),],
        }

        self.move(0, 3)

class U5_block(Block):
    def __init__(self):
        super().__init__(id = 4)

        self.cells = {
            0:[Position(0,0),Position(0,1),Position(0,2),Position(1,0),Position(1,2),],
            1:[Position(0,1),Position(0,2),Position(1,2),Position(2,1),Position(2,2),],
            2:[Position(1,0),Position(1,2),Position(2,0),Position(2,1),Position(2,2),],
            3:[Position(0,0),Position(0,1),Position(1,0),Position(2,0),Position(2,1),],
        }

        self.move(0, 3)

class W5_block(Block):
    def __init__(self):
        super().__init__(id = 5)

        self.cells = {
            0:[Position(0,2),Position(1,1),Position(1,2),Position(2,0),Position(2,1),],
            1:[Position(0,0),Position(1,0),Position(1,1),Position(2,1),Position(2,2),],
            2:[Position(0,1),Position(0,2),Position(1,0),Position(1,1),Position(2,0),],
            3:[Position(0,0),Position(0,1),Position(1,1),Position(1,2),Position(2,2),],
        }

        self.move(0, 3)

class X5_block(Block):
    def __init__(self):
        super().__init__(id = 6)

        self.cells = {
            0:[Position(0,1),Position(1,0),Position(1,1),Position(1,2),Position(2,1),],
        }

        self.move(0, 3)

class J5_block(Block):
    def __init__(self):
        super().__init__(id = 7)

        self.cells = {
            0:[Position(0,0),Position(1,0),Position(1,1),Position(1,2),Position(1,3),],
            1:[Position(0,1),Position(0,2),Position(1,1),Position(2,1),Position(3,1),],
            2:[Position(1,0),Position(1,1),Position(1,2),Position(1,3),Position(2,3),],
            3:[Position(0,1),Position(1,1),Position(2,1),Position(3,1),Position(3,0),],
        }

        self.move(0, 3)

class L5_block(Block):
    def __init__(self):
        super().__init__(id = 1)

        self.cells = {
            0:[Position(0,3),Position(1,0),Position(1,1),Position(1,2),Position(1,3),],
            1:[Position(0,1),Position(1,1),Position(2,1),Position(3,1),Position(3,2),],
            2:[Position(1,0),Position(1,1),Position(1,2),Position(1,3),Position(2,0),],
            3:[Position(0,0),Position(0,1),Position(1,1),Position(2,1),Position(3,1),],
        }

        self.move(0, 3)