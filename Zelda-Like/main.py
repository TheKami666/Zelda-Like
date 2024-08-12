import pygame
import sys
import math
from Player import Player
from Livelli.Livelli import Livello1
from dialogo import Dialogo

pygame.init()

LARGHEZZA_FINESTRA = 800
ALTEZZA_FINESTRA = 600
VELOCITA_GIOCATORE = 2
FINESTRA = pygame.display.set_mode((LARGHEZZA_FINESTRA, ALTEZZA_FINESTRA))
CLOCK = pygame.time.Clock()
pygame.display.set_caption("PALLE")


livello1 = Livello1(LARGHEZZA_FINESTRA, ALTEZZA_FINESTRA)
player = Player(LARGHEZZA_FINESTRA, ALTEZZA_FINESTRA, VELOCITA_GIOCATORE, livello1)
dialogo = Dialogo()

run = True
while run:
    eventi = pygame.event.get()
    for evento in eventi:
        if evento.type == pygame.QUIT:
            run = False

    livello1.gestisci_input(eventi)
    livello1.aggiorna(FINESTRA)

    player.muovi()
    player.disegna(FINESTRA)

    pygame.display.flip()
    CLOCK.tick(60)

pygame.quit()
sys.exit()
