from base_tetris.game import Game
import pygame

class Marathon(Game):
    def __init__(self):
        super().__init__()
        self.level = 0 
        self.lines_cleared_total = 0 
        # self.fall_speed = 1000  # initial fall speed (in milliseconds)(1 second) 
    
    # when rows are cleared, add to the total lines cleared 
    def add_lines(self, num_lines):
        self.lines_cleared_total += num_lines
        self.level = self.lines_cleared_total // 5 # (increase level every 5 lines)
        self.increase_fall_speed()

    def increase_fall_speed(self):
        initial_speed = 500 # moves down one every second 
        self.fall_speed = initial_speed - (self.level * 50) # every level increase, the fall speed will increase 

        if self.fall_speed < 100: # so it doesn't get too fast 
            self.fall_speed = 100

        pygame.time.set_timer(pygame.USEREVENT, self.fall_speed)


