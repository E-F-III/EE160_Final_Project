import random
from base_tetris.game import Game
from .pentominoes import *

blocks = [I5_block(), V5_block(), X5_block(), T5_block(), U5_block(),
          W5_block(), J5_block(), L5_block(), S5_block(), Z5_block(),
          TL_block(), TJ_block()]

class Pentrix(Game):
    def __init__(self):
        super().__init__()
        self.blocks = [TJ_block()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [TJ_block()]

        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)