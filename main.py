# importation des librairie
import pygame
import pygame_menu

pygame.init()  # initialisation de pygame


def set_difficulty(value, difficulty):
    # changement difficulté
    pass


def start_the_game():
    # lancement du jeu
    pass


# creation de la fenetre et de son titre
pygame.display.set_caption("JEUX MINOU")
screen = pygame.display.set_mode((1280, 700))
image_menu = pygame.image.load("image/fond_menu.jpg")  # importation de l'image
image_menu = pygame.transform.scale(image_menu, (1280, 700))
pygame.display.update()  # mise a jour de l'écran (refresh)
menu = pygame_menu.Menu("Bonjour", 1280, 700, theme=pygame_menu.themes.THEME_BLUE)
menu.add.text_input("Name :", default="Quentin")
menu.add.selector("Difficulty :", [("Hard", 1), ("Easy", 2)], onchange=set_difficulty)
menu.add.button("Play", start_the_game)
menu.add.button("Quit", pygame_menu.events.EXIT)
menu.mainloop(screen)

# run = True
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#             pygame.exit
