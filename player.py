import pygame
import math

class Player():
    
    def __init__(self,x,y,image):
        self.image = image
        self.rect = image.get_rect(x=x,y=y)
        self.speed = 200
        
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
        
    def move(self, dt):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_d]:
            self.rect.x += self.speed * dt
        if pressed[pygame.K_a]:
            self.rect.x -= self.speed * dt
        if pressed[pygame.K_w]:
            self.rect.y -= self.speed * dt
        if pressed[pygame.K_s]:
            self.rect.y += self.speed * dt