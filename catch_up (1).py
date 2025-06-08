import pygame
from player import *
from enemy import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("donie dumb killer game")
bg = pygame.image.load("buffalo.jpg")
bg = pygame.transform.scale(bg, (800, 600))

#player
p1 = pygame.image.load("Emu.png")
p1 = pygame.transform.scale(p1 ,(175,175))


player = Player(0,0, p1)



clock = pygame.time.Clock()


ghost = pygame.image.load("trump.png")
ghost = pygame.transform.scale(ghost,(180,180))
enemy = Enemy(600,0,ghost)


running = True
while (running) :
    dt = clock.tick(60) / 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg,(0,0))
    player.draw(screen)
    player.move(dt)
    enemy.draw(screen)
    enemy.move(dt)
    pygame.display.update()
pygame.quit()