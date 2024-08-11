import pygame
import sys
import math
from Player import Player
from Livelli.Livelli import Livello1

pygame.init()

LARGHEZZA_FINESTRA = 800
ALTEZZA_FINESTRA = 600
VELOCITA_GIOCATORE = 2
FINESTRA = pygame.display.set_mode((LARGHEZZA_FINESTRA, ALTEZZA_FINESTRA))
CLOCK = pygame.time.Clock()
pygame.display.set_caption("PALLE")

player = Player(LARGHEZZA_FINESTRA, ALTEZZA_FINESTRA, VELOCITA_GIOCATORE)
livello1 = Livello1(LARGHEZZA_FINESTRA, ALTEZZA_FINESTRA)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player.muovi()

    livello1.disegna(FINESTRA)

    player.disegna(FINESTRA)

    pygame.display.flip()
    CLOCK.tick(60)

pygame.quit()
sys.exit()
