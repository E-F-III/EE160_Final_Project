from base_tetris.game import Game
from base_tetris.tetrimino import *
from .chaos_block import *
import random
from pentix.pentominos import *

class Chaos(Game):
    def __init__(self):
        super().__init__()
        self.inverted_controls = False
        self.blocks=[ChaosLBlock(),
                     ChaosJBlock(),
                     ChaosIBlock(),
                     ChaosOBlock(),
                     ChaosSBlock(),
                     ChaosTBlock(),
                     ChaosZBlock(),]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        
    def get_random_block(self):
       
        if len(self.blocks) == 0:
            self.blocks=[ChaosLBlock(),
                     ChaosJBlock(),
                     ChaosIBlock(),
                     ChaosOBlock(),
                     ChaosSBlock(),
                     ChaosTBlock(),
                     ChaosZBlock(),]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
            
        
    def reset(self):
       self.grid.reset()
       self.blocks=[ChaosLBlock(),
                     ChaosJBlock(),
                     ChaosIBlock(),
                     ChaosOBlock(),
                     ChaosSBlock(),
                     ChaosTBlock(),
                     ChaosZBlock(),]
       self.current_block = self.get_random_block()
       self.next_block = self.get_random_block()
       self.score = 0
       
    def move_right(self):
        if not self.inverted_controls:
           self.current_block.move(0, 1)
           if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0,-1)
        else:
           self.current_block.move(0, -1)
           if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0,1)


    def move_left(self):
        # if statements for checking if controls are inverted, and moving left if not, moveing right if it is
        if not self.inverted_controls:
           self.current_block.move(0, -1)
           if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0,1)
        else:
           self.current_block.move(0, 1)
           if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0,-1)
    
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks=[ChaosLBlock(),
                     ChaosJBlock(),
                     ChaosIBlock(),
                     ChaosOBlock(),
                     ChaosSBlock(),
                     ChaosTBlock(),
                     ChaosZBlock(),]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        # logic that runs to randomly switch between inverted controls or non inverted controls when a new block is selected
        self.inverted_controls = random.choice([True, False])
        return block

    def lock_block(self):
        # super().lock_block()
        self.fall_speed = random.randint(20, 500)

        # tiles = self.current_block.get_cell_positions()
        # for i in range(len(tiles)):
        #     position = tiles[i]
        #     self.grid.grid[position.row][position.column] = self.current_block.randomcolors[i]
        # self.current_block = self.next_block
        # self.next_block = self.get_random_block()
        # rows_cleared = self.grid.clear_full_rows()

        tiles = self.current_block.get_cell_positions()
        for i in range(len(tiles)):
            position = tiles[i]
            self.grid.grid[position.row][position.column] = self.current_block.randomcolors[i]
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        
        self.update_score(rows_cleared, 0)
        if hasattr(self, 'add_lines'):
            self.add_lines(rows_cleared)

        if self.block_fits() == False:
            self.game_over = True