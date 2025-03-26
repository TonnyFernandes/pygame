import pygame
from random import randint as rd
from settings import *

class Projectile:
    def __init__(self):
        # Choose in wish edge the projectile will spawn, once the class is called
        #   0: top, moving downward
        #   1: right, moving leftward
        #   2: bottom, moving upward
        #   3: left, moving rightward
        edge = rd(0, 3)
        match (edge):
            case 0:
                self.x = rd(0, SCREEN_WIDTH - PROJECTILE_SIZE)
                self.y = -PROJECTILE_SIZE
                self.dx, self.dy = 0, PROJECTILE_SPEED
            case 1:
                self.x = SCREEN_WIDTH
                self.y = rd(0, SCREEN_HEIGHT - PROJECTILE_SIZE)
                self.dx, self.dy = -PROJECTILE_SPEED, 0
            case 2:
                self.x = rd(0, SCREEN_WIDTH - PROJECTILE_SIZE)
                self.y = SCREEN_HEIGHT
                self.dx, self.dy = 0, -PROJECTILE_SPEED
            case 3:
                self.x = -PROJECTILE_SIZE
                self.y = rd(0, SCREEN_HEIGHT - PROJECTILE_SIZE)
                self.dx, self.dy = PROJECTILE_SPEED, 0

        self.rect = pygame.Rect(self.x, self.y, PROJECTILE_SIZE, PROJECTILE_SIZE)

    def update(self) -> None:
        self.rect.x += self.dx
        self.rect.y += self.dy
    
    def is_off_screen(self) -> bool:
        return (self.rect.right < 0 or
                self.rect.left > SCREEN_WIDTH or
                self.rect.bottom < 0 or
                self.rect.top > SCREEN_HEIGHT)
    
    def draw(self, screen) -> None:
        pygame.draw.rect(screen, RED, self.rect)