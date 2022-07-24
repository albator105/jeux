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
image_menu = pygame_menu.baseimage.BaseImage(
    image_path=("image/fond_menu.jpg")
)
menu_theme = pygame_menu.Theme(background_color=image_menu, # transparent background
                title_background_color=(225, 98, 117),
                title_font_shadow=True,
                widget_padding=25)
# creation de la fenetre et de son titre
pygame.display.set_caption("JEUX MINOU")
pygame.mixer.music.load("son/music1.mp3")
screen = pygame.display.set_mode((1280, 700),pygame.FULLSCREEN)
menu = pygame_menu.Menu("Dragon Breath", 1280, 700,theme=menu_theme)
menu.add.text_input("Name :", default="")
menu.add.selector("Difficulty :", [("Facile", 1), ("Moyen", 2)], onchange=set_difficulty)
menu.add.button("Play", start_the_game)
menu.add.button("Quit", pygame_menu.events.EXIT)
menu.add.button("music stop", pygame.mixer.music.stop)
menu.add.button("music start", pygame.mixer.music.play)
pygame.display.update()  # mise a jour de l'écran (refresh)
menu.mainloop(screen)
