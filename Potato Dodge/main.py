import pygame
import os
from settings import *
from projectile import Projectile

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class PotatoGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.load_assets()
        self.reset_game()

    def load_assets(self):
        # Set the path for current directory and the path to all images
        script_dir = os.path.dirname(os.path.abspath(__file__))
        potato_path = os.path.join(script_dir, 'imgs', 'potato.png')
        self.record_path = os.path.join(script_dir, 'record.txt')
        # open and personalize the potato image
        try:
            self.potato_img = pygame.image.load(potato_path).convert_alpha()
            self.potato_img = pygame.transform.scale(self.potato_img, (POTATO_SIZE, POTATO_SIZE))
        except FileNotFoundError:
            print(f'ERROR: Could not load image at {potato_path}')
            pygame.quit()
            exit()
    
    def reset_game(self):
        self.potato_pos = [SCREEN_WIDTH//2, SCREEN_HEIGHT//2]
        self.projectiles = []
        self.spawn_timer = 0
        self.running = True
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self):
        # Move potato
        keys = pygame.key.get_pressed()
        self.potato_pos[0] += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * POTATO_SPEED
        self.potato_pos[1] += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * POTATO_SPEED
        
        # Boundaries
        self.potato_pos[0] = max(0, min(self.potato_pos[0], SCREEN_WIDTH - POTATO_SIZE))
        self.potato_pos[1] = max(0, min(self.potato_pos[1], SCREEN_HEIGHT - POTATO_SIZE))
        
        # Spawn projectiles
        self.spawn_timer += 1
        if self.spawn_timer >= SPAWN_INTERVAL:
            self.spawn_timer = 0
            self.projectiles.append(Projectile())
        
        # Update projectiles
        for proj in self.projectiles[:]:
            proj.update()
            if proj.is_off_screen():
                self.projectiles.remove(proj)
            
            # Collision check
            potato_rect = pygame.Rect(*self.potato_pos, POTATO_SIZE, POTATO_SIZE)
            if potato_rect.colliderect(proj.rect):
                print("Game Over!")
                self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.potato_img, self.potato_pos)
        for proj in self.projectiles:
            proj.draw(self.screen)
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

if __name__ == "__main__":
    game = PotatoGame()
    game.run()