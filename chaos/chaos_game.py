from base_tetris.game import Game
import random
import pygame

class Chaos(Game):
    def __init__(self):
        super().__init__()
    
    def lock_block(self):
        super().lock_block()

        # Randomize fall speed for the next block (normal to very fast)
        self.fall_speed = random.randint(20, 500)