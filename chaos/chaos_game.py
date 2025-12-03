from base_tetris.game import Game
import random

class Chaos(Game):
    def __init__(self):
        super().__init__()

    def lock_block(self):
        super().lock_block()
        self.fall_speed = random.randint(20, 500)