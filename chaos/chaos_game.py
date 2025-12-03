from base_tetris.game import Game
from base_tetris.tetrimino import *
import random

class Chaos(Game):
    def __init__(self):
        super().__init__()
        self.inverted_controls = False

    def move_left(self):
        # if statements for checking if controls are inverted, and moving left if not, moveing right if it is
        if not self.inverted_controls:
           self.current_block.move(0, -1)
        else:
           self.current_block.move(0, 1)


        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0,1)
    
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        # logic that runs to randomly switch between inverted controls or non inverted controls when a new block is selected
        self.inverted_controls == random.choice([True, False])
        return block

    def lock_block(self):
        super().lock_block()
        self.fall_speed = random.randint(20, 500)