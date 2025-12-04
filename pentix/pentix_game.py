import random
from base_tetris.game import Game
from .pentominos import *

blocks = [I5_block(), V5_block(), X5_block(), T5_block(), U5_block(),
          W5_block(), J5_block(), L5_block(), S5_block(), Z5_block(),
          TL_block(), TJ_block(), OZ_block(), OS_block(), TS_block(),
          TZ_block(), LL_block(), JJ_block()]

class Pentrix(Game):
    """
    Pentrix game class, inherits from the base Game class.
    """
    def __init__(self):
        """
        Initialize the Pentrix game with a grid and a set of pentomino blocks.
        """
        super().__init__()
        self.blocks = [I5_block(), V5_block(), X5_block(), T5_block(), U5_block(),
          W5_block(), J5_block(), L5_block(), S5_block(), Z5_block(),
          TL_block(), TJ_block(), OZ_block(), OS_block(), TS_block(),
          TZ_block(), LL_block(), JJ_block()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def get_random_block(self):
        """
        Get a random pentomino block from the available blocks.
        """
        if len(self.blocks) == 0:
            self.blocks = [I5_block(), V5_block(), X5_block(), T5_block(), U5_block(),
          W5_block(), J5_block(), L5_block(), S5_block(), Z5_block(),
          TL_block(), TJ_block(), OZ_block(), OS_block(), TS_block(),
          TZ_block(), LL_block(), JJ_block()]

        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def reset(self):
        """
        Reset the game state, including the grid, blocks, current and next blocks, and score.
        """
        self.grid.reset()
        self.blocks = [I5_block(), V5_block(), X5_block(), T5_block(), U5_block(),
          W5_block(), J5_block(), L5_block(), S5_block(), Z5_block(),
          TL_block(), TJ_block(), OZ_block(), OS_block(), TS_block(),
          TZ_block(), LL_block(), JJ_block()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def draw(self, screen):
        """
        Draw the game state on the screen.
        """
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        if isinstance(self.next_block, I5_block):  
            self.next_block.draw(screen, 245, 270)
        elif isinstance(self.next_block, X5_block):
            self.next_block.draw(screen, 255, 280)
        elif isinstance(self.next_block, (TL_block, TJ_block, OZ_block, OS_block, TS_block, TZ_block)):
            self.next_block.draw(screen, 255, 275)
        elif isinstance(self.next_block, (LL_block, JJ_block)):
            self.next_block.draw(screen, 255, 280)
        elif isinstance(self.next_block, (V5_block, T5_block, U5_block, W5_block, J5_block, L5_block, S5_block, Z5_block)):
            self.next_block.draw(screen, 260, 270)
        else:
            self.next_block.draw(screen, 255, 270)