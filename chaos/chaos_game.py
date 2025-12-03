from base_tetris.game import Game
import random

class Chaos(Game):
    def __init__(self):
        super().__init__()
    
    def lock_block(self):
        super().lock_block()

        #randomize fall speed for the next block (normal to very fast)
        self.fall_speed = random.choice([500, 50])