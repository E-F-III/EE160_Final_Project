import pygame
import sys
from base_tetris.game import Game
from base_tetris.colors import Colors
from pentix.pentix_game import Pentrix
from marathon.marathon_game import Marathon
from chaos.chaos_game import Chaos

pygame.init()

# Fonts
title_font = pygame.font.Font(None, 40)
menu_font = pygame.font.Font(None, 60)
menu_item_font = pygame.font.Font(None, 50)

# Screen setup
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

# Game states
STATE_MENU = "menu"
STATE_PLAYING = "playing"

class GameManager:
    def __init__(self):
        self.state = STATE_MENU
        self.game = None
        self.game_mode = None
        self.selected_menu_item = 0
        self.menu_items = ["Marathon", "Chaos", "Pentrix", "Quit"]
        
        # UI surfaces
        self.score_surface = title_font.render("Score", True, Colors.white)
        self.next_surface = title_font.render("Next", True, Colors.white)
        self.game_over_surface = title_font.render("Game Over", True, Colors.white)
        self.level_surface = title_font.render("Level", True, Colors.white)

        # UI rects
        self.score_rect = pygame.Rect(320, 55, 170, 60)
        self.next_rect = pygame.Rect(320, 215, 170, 180)
        self.level_rect = pygame.Rect(320, 450, 170, 60)
        
        # Game timer
        self.GAME_UPDATE = pygame.USEREVENT
        
    def start_game(self, mode):
        """Initialize game based on selected mode"""
        self.game_mode = mode
        
        if mode == "Marathon":
            self.game = Marathon()
        elif mode == "Chaos":
            self.game = Chaos()
        elif mode == "Pentrix":
            self.game = Pentrix()
        
        self.state = STATE_PLAYING
        pygame.time.set_timer(self.GAME_UPDATE, self.game.fall_speed)
    
    def return_to_menu(self):
        """Return to main menu"""
        self.state = STATE_MENU
        self.game = None
        self.game_mode = None
        pygame.time.set_timer(self.GAME_UPDATE, 0)  # Stop game timer
    
    def handle_menu_input(self, event):
        """Handle input in menu state"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_menu_item = (self.selected_menu_item - 1) % len(self.menu_items)
            elif event.key == pygame.K_DOWN:
                self.selected_menu_item = (self.selected_menu_item + 1) % len(self.menu_items)
            elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                selected = self.menu_items[self.selected_menu_item]
                if selected == "Quit":
                    pygame.quit()
                    sys.exit()
                else:
                    self.start_game(selected)
    
    def handle_game_input(self, event):
        """Handle input in playing state"""
        if event.type == pygame.KEYDOWN:
            # ESC to return to menu
            if event.key == pygame.K_ESCAPE:
                self.return_to_menu()
                return
            
            if self.game.game_over:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    self.game.game_over = False
                    self.game.reset()
            else:
                if event.key == pygame.K_LEFT:
                    self.game.move_left()
                elif event.key == pygame.K_RIGHT:
                    self.game.move_right()
                elif event.key == pygame.K_DOWN:
                    self.game.move_down()
                    self.game.update_score(0, 1)
                elif event.key == pygame.K_UP or event.key == pygame.K_x:
                    self.game.rotate()
                elif event.key == pygame.K_z:
                    self.game.rotate_counterclockwise()
                elif event.key == pygame.K_SPACE:
                    self.game.instant_drop()
        
        # if event.type == self.GAME_UPDATE and not self.game.game_over:
        #     self.game.move_down()
    
    def draw_menu(self):
        """Draw the main menu"""
        screen.fill(Colors.dark_blue)
        
        # Title
        title_surface = menu_font.render("TETRIS", True, Colors.white)
        title_rect = title_surface.get_rect(center=(250, 100))
        screen.blit(title_surface, title_rect)
        
        # Menu items
        for i, item in enumerate(self.menu_items):
            color = Colors.yellow if i == self.selected_menu_item else Colors.white
            item_surface = menu_item_font.render(item, True, color)
            item_rect = item_surface.get_rect(center=(250, 250 + i * 70))
            screen.blit(item_surface, item_rect)
        
        # Instructions
        instruction_font = pygame.font.Font(None, 25)
        instructions = instruction_font.render("Use Arrow Keys and Enter", True, Colors.light_blue)
        instructions_rect = instructions.get_rect(center=(250, 550))
        screen.blit(instructions, instructions_rect)
    
    def draw_game(self):
        """Draw the game screen"""
        screen.fill(Colors.dark_blue)
        
        # Score and next piece UI
        screen.blit(self.score_surface, (365, 20, 50, 50))
        screen.blit(self.next_surface, (375, 180, 50, 50))
        
        pygame.draw.rect(screen, Colors.light_blue, self.score_rect, 0, 10)
        pygame.draw.rect(screen, Colors.light_blue, self.next_rect, 0, 10)
        
        # Score value
        score_value_surface = title_font.render(str(self.game.score), True, Colors.white)
        screen.blit(score_value_surface, 
                   score_value_surface.get_rect(centerx=self.score_rect.centerx, 
                                                centery=self.score_rect.centery))
        
        if self.game_mode == "Marathon":
            screen.blit(self.level_surface, (365, 420, 50, 50))
            pygame.draw.rect(screen, Colors.light_blue, self.level_rect, 0, 10)
            level_value_surface = title_font.render(str(self.game.level), True, Colors.white)
            screen.blit(level_value_surface, 
                       level_value_surface.get_rect(centerx=self.level_rect.centerx, 
                                                    centery=self.level_rect.centery))
        # Game over message
        if self.game.game_over:
            screen.blit(self.game_over_surface, (320, 550, 50, 50))
            
            # # Add restart/menu instructions
            # instruction_font = pygame.font.Font(None, 25)
            # restart_text = instruction_font.render("Space: Restart | ESC: Menu", True, Colors.white)
            # restart_rect = restart_text.get_rect(center=(250, 500))
            # screen.blit(restart_text, restart_rect)
        
        # Draw game
        self.game.draw(screen)
    
    def run(self):
        """Main game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if self.state == STATE_MENU:
                    self.handle_menu_input(event)
                elif self.state == STATE_PLAYING:
                    self.handle_game_input(event)
            
            # Drawing
            if self.state == STATE_MENU:
                self.draw_menu()
            elif self.state == STATE_PLAYING:
                self.draw_game()
            
            delta_time = clock.tick(60) / 1000
            if self.state == STATE_PLAYING and not self.game.game_over:
                self.game.fall_time += delta_time

                if self.game.fall_time >= self.game.fall_speed / 1000:
                    self.game.move_down()
                    self.game.fall_time = 0

            pygame.display.update()
            

# Run the game
if __name__ == "__main__":
    game_manager = GameManager()
    game_manager.run()