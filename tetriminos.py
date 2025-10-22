from block import Block
from position import Position

class L_block(Block):
    def __init__(self):
        super().__init__(id = 1)
        # self.cells is a dct that contains the different orientations the Tetrimino can be 
        self.cells = {
            0: [Position(0,2), Position(1, 0), Position(1,1), Position(1, 2)],
            1: [Position(0,1), Position(1, 1), Position(2,1), Position(2, 2)],
            2: [Position(1,0), Position(1, 1), Position(1,2), Position(2, 0)],
            3: [Position(0,0), Position(0, 1), Position(1,1), Position(2, 1)]
        }
        self.move(0, 3) # spawns block at top center of the grid 

class J_block(Block):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0: [Position(0,0), Position(1, 0), Position(1,1), Position(1, 2)],
            1: [Position(0,1), Position(0, 2), Position(1,1), Position(2, 1)],
            2: [Position(1,0), Position(1, 1), Position(1,2), Position(2, 2)],
            3: [Position(0,1), Position(1, 1), Position(2,0), Position(2, 1)]
        }
        self.move(0, 3) # spawns block at top center of the grid 

class I_block(Block):
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0: [Position(1,0), Position(1, 1), Position(1,2), Position(1, 3)],
            1: [Position(0,2), Position(1, 2), Position(2,2), Position(3, 2)],
            2: [Position(2,0), Position(2, 1), Position(2,2), Position(2, 3)],
            3: [Position(0,1), Position(1, 1), Position(2,1), Position(3, 1)]
        }
        self.move(-1, 3) # spawns block at top center of the grid 

class O_block(Block):
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            0: [Position(0,0), Position(0, 1), Position(1,0), Position(1, 1)],
            1: [Position(0,0), Position(0, 1), Position(1,0), Position(1, 1)],
            2: [Position(0,0), Position(0, 1), Position(1,0), Position(1, 1)],
            3: [Position(0,0), Position(0, 1), Position(1,0), Position(1, 1)]
        }
        self.move(0, 4) # spawns block at top center of the grid 

class S_block(Block):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0: [Position(0,1), Position(0, 2), Position(1,0), Position(1, 1)],
            1: [Position(0,1), Position(1, 1), Position(1,2), Position(2, 2)],
            2: [Position(1,1), Position(1, 2), Position(2,0), Position(2, 1)],
            3: [Position(0,0), Position(1, 0), Position(1,1), Position(2, 1)]
        }
        self.move(0, 3) # spawns block at top center of the grid 

class T_block(Block):
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0: [Position(0,1), Position(1, 0), Position(1,1), Position(1, 2)],
            1: [Position(0,1), Position(1, 1), Position(1,2), Position(2, 1)],
            2: [Position(1,0), Position(1, 1), Position(1,2), Position(2, 1)],
            3: [Position(0,1), Position(1, 0), Position(1,1), Position(2, 1)]
        }
        self.move(0, 3) # spawns block at top center of the grid 

class Z_block(Block):
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            0: [Position(0,0), Position(0, 1), Position(1,1), Position(1, 2)],
            1: [Position(0,2), Position(1, 1), Position(1,2), Position(2, 1)],
            2: [Position(1,0), Position(1, 1), Position(2,1), Position(2, 2)],
            3: [Position(0,1), Position(1, 0), Position(1,1), Position(2, 0)]
        }
        self.move(0, 3) # spawns block at top center of the grid 


