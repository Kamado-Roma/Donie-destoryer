import pygame
import math

class Enemy():
    
    def __init__(self,x,y,image):
        self.image = image
        self.rect = image.get_rect(x=x,y=y)
        self.speed = 200
        
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
        
    def move(self, dt):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed * dt
        if pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed * dt
        if pressed[pygame.K_UP]:
            self.rect.y -= self.speed * dt
        if pressed[pygame.K_DOWN]:
            self.rect.y += self.speed * dt