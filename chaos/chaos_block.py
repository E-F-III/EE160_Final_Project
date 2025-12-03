from base_tetris.tetrimino import *
import pygame
import random

class ChaosLBlock(LBlock):
    def __init__(self):
        super().__init__()
        self.randomcolors = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]

    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for i in range(len(tiles)): 
            tile = tiles[i]
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, 
                                    offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1) 
            pygame.draw.rect(screen, self.colors[self.randomcolors[i]], tile_rect)
 
class ChaosJBlock(JBlock):
    def __init__(self):
        super().__init__()
        self.randomcolors = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]

    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for i in range(len(tiles)): 
            tile = tiles[i]
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, 
                                    offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1) 
            pygame.draw.rect(screen, self.colors[self.randomcolors[i]], tile_rect)
 
class ChaosIBlock(IBlock):
    def __init__(self):
        super().__init__()
        self.randomcolors = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]

    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for i in range(len(tiles)): 
            tile = tiles[i]
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, 
                                    offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1) 
            pygame.draw.rect(screen, self.colors[self.randomcolors[i]], tile_rect)
 
class ChaosOBlock(OBlock):
    def __init__(self):
        super().__init__()
        self.randomcolors = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]

    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for i in range(len(tiles)): 
            tile = tiles[i]
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, 
                                    offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1) 
            pygame.draw.rect(screen, self.colors[self.randomcolors[i]], tile_rect)
 
class ChaosSBlock(SBlock):
    def __init__(self):
        super().__init__()
        self.randomcolors = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]

    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for i in range(len(tiles)): 
            tile = tiles[i]
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, 
                                    offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1) 
            pygame.draw.rect(screen, self.colors[self.randomcolors[i]], tile_rect)
 
class ChaosTBlock(TBlock):
    def __init__(self):
        super().__init__()
        self.randomcolors = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]

    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for i in range(len(tiles)): 
            tile = tiles[i]
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, 
                                    offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1) 
            pygame.draw.rect(screen, self.colors[self.randomcolors[i]], tile_rect)
 
class ChaosZBlock(ZBlock):
    def __init__(self):
        super().__init__()
        self.randomcolors = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]

    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for i in range(len(tiles)): 
            tile = tiles[i]
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, 
                                    offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1) 
            pygame.draw.rect(screen, self.colors[self.randomcolors[i]], tile_rect)
 

    
