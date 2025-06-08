import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("gyatt catcher game")
bg = pygame.image.load("buffalo.jpg")
bg = pygame.transform.scale(bg, (800, 600))

#player
p1 = pygame.image.load("Emu.png")
p1 = pygame.transform.scale(p1 ,(175,175))
ghost = pygame.image.load("trump.png")
ghost = pygame.transform.scale(ghost,(180,180))


running = True
while (running) :
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg,(0,0))
    screen.blit(p1, (0,0))
    screen.blit(ghost,(600,0))
    pygame.display.update()
pygame.quit()