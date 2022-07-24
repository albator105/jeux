import pygame
pygame.init()
screen = pygame.display.set_mode((1080, 500))
pygame.display.set_caption('JEUX MINOU')
pygame.display.update()
run = True
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
exit
        