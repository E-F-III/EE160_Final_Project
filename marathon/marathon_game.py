from base_tetris.game import Game

class Marathon(Game):
    def __init__(self):
        super().__init__()
        self.level = 0 
        self.lines_cleared_total = 0 
        self.fall_speed = 2000  # initial fall speed (in milliseconds)(1 second) 

    def increase_fall_speed(self):
        initial_speed = 2000 # moves down one every second 
        self.fall_speed = initial_speed - (self.level * 50) # every level increase, the fall speed will increase 

        if self.fall_speed < 100: # so it doesn't get too fast 
            self.fall_speed = 100

    # when rows are cleared, add to the total lines cleared 
    def add_lines(self, num_lines):
        self.lines_cleared_total += num_lines
        self.level = self.lines_cleared_total // 10 # (increase level every 10 lines)
        self.increase_fall_speed()

# why is it still super fast 
