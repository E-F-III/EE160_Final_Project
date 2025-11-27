import random
from base_tetris.game import Game
from .pentominos import *

blocks = [I5_block(), V5_block(), X5_block(), T5_block(), U5_block(),
          W5_block(), J5_block(), L5_block(), S5_block(), Z5_block(),
          TL_block(), TJ_block(), OZ_block(), OS_block(), TS_block(),
          TZ_block(), LL_block(), JJ_block()]

class Pentrix(Game):
    def __init__(self):
        super().__init__()
        self.blocks = [I5_block(), V5_block(), X5_block(), T5_block(), U5_block(),
          W5_block(), J5_block(), L5_block(), S5_block(), Z5_block(),
          TL_block(), TJ_block(), OZ_block(), OS_block(), TS_block(),
          TZ_block(), LL_block(), JJ_block()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [I5_block(), V5_block(), X5_block(), T5_block(), U5_block(),
          W5_block(), J5_block(), L5_block(), S5_block(), Z5_block(),
          TL_block(), TJ_block(), OZ_block(), OS_block(), TS_block(),
          TZ_block(), LL_block(), JJ_block()]

        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def reset(self):
        self.grid.reset()
        self.blocks = [I5_block(), V5_block(), X5_block(), T5_block(), U5_block(),
          W5_block(), J5_block(), L5_block(), S5_block(), Z5_block(),
          TL_block(), TJ_block(), OZ_block(), OS_block(), TS_block(),
          TZ_block(), LL_block(), JJ_block()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)