import pygame

class Conway:
    """
    Classe de gestion d'un plateau de jeu de la vie
    """

    def __init__(self, surface):
        self.surface = surface

    def dessine(self):
        pygame.draw.rect(self.surface, (200, 200, 200), pygame.Rect(262,134, 500, 500))
