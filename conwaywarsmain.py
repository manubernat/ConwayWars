import os
import sys
import pygame
import conway

def conwaywarsgame():
    """
    Fonction principale de Conway Wars
    """
    # Initialisation de PyGame
    npass, nfail = pygame.init()

    # Quitte si un module n'est pas initialisé
    if nfail>0:
        print("Il manque des modules PyGame : abandon du jeu")
        sys.exit()

    # Création de l'écran de jeu et titre de la fenêtre
    screen = pygame.display.set_mode((1024,768))
    pygame.display.set_caption('Conway Wars')

    # Création du fond (noir)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Création du titre
    font = pygame.font.Font(None, 36)
    text = font.render("Conway Wars", 1, (180, 180, 180))
    textpos = text.get_rect(centerx=background.get_width()/2)
    background.blit(text, textpos)

    # Horloge du jeu
    clock = pygame.time.Clock()

    # Boucle principale
    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.blit(background, (0, 0))
        pygame.display.flip()


# Lance le jeu si le fichier est le module principal
if __name__=="__main__":
    conwaywarsgame()

