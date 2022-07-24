#importation des librairie
import pygame
pygame.init() #initialisation de pygame


#creation de la fenetre et de son titre
screen = pygame.display.set_mode((1280, 700))
pygame.display.set_caption('JEUX MINOU')

image_menu = pygame.image.load("image/fond_menu.jpg") # importation de l'image
image_menu = pygame.transform.scale(image_menu, (1280,700))
screen.blit(image_menu, (0,0))
pygame.display.update() # mise a jour de l'écran (refresh)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.exit


        