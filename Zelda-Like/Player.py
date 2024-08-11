import pygame
import math

class Player:
    def __init__(self, larghezza_finestra, altezza_finestra, velocita_giocatore):
        self.larghezza_finestra = larghezza_finestra
        self.altezza_finestra = altezza_finestra
        self.velocita = velocita_giocatore
        self.x = larghezza_finestra // 2
        self.y = altezza_finestra // 2
        self.animazione_corrente = 0
        self.sprite_sheet = pygame.image.load('gfx/NPC_test.png').convert_alpha()

        DIM_FRAME_SPRITE_PG = (16, 32)
        NUM_COLONNE = 4
        NUM_RIGHE = 4
        SCALA = 3

        self.frames = []
        for riga in range(NUM_RIGHE):
            for colonna in range(NUM_COLONNE):
                rect = pygame.Rect(colonna * DIM_FRAME_SPRITE_PG[0], riga * DIM_FRAME_SPRITE_PG[1], DIM_FRAME_SPRITE_PG[0], DIM_FRAME_SPRITE_PG[1])
                frame = self.sprite_sheet.subsurface(rect)
                frame_scalato = pygame.transform.scale(frame, (DIM_FRAME_SPRITE_PG[0] * SCALA, DIM_FRAME_SPRITE_PG[1] * SCALA))
                self.frames.append(frame_scalato)

        self.direzioni = {
            'su': [8, 9, 10, 11],
            'giu': [0, 1, 2, 3],
            'sinistra': [12, 13, 14, 15],
            'destra': [4, 5, 6, 7]
        }

        self.direzione_corrente = 'giu'
        self.frame_attuale = 0
        self.larghezza_sprite = DIM_FRAME_SPRITE_PG[0] * SCALA
        self.altezza_sprite = DIM_FRAME_SPRITE_PG[1] * SCALA
        self.tempo_ultimo_frame = pygame.time.get_ticks()
        self.tempo_frame = 100

    def disegna(self, schermo):
        frame_index = self.direzioni[self.direzione_corrente][self.frame_attuale]
        schermo.blit(self.frames[frame_index], (self.x, self.y))

    def muovi(self):
        keys = pygame.key.get_pressed()
        movimento_x = 0
        movimento_y = 0

        if keys[pygame.K_LSHIFT]:
            velocita_corrente = self.velocita * 2
        else:
            velocita_corrente = self.velocita

        if keys[pygame.K_a]:
            movimento_x -= velocita_corrente
            self.direzione_corrente = 'sinistra'
        if keys[pygame.K_s]:
            movimento_y += velocita_corrente
            self.direzione_corrente = 'giu'
        if keys[pygame.K_d]:
            movimento_x += velocita_corrente
            self.direzione_corrente = 'destra'
        if keys[pygame.K_w]:
            movimento_y -= velocita_corrente
            self.direzione_corrente = 'su'

        if movimento_x != 0 and movimento_y != 0:
            movimento_x /= math.sqrt(2)
            movimento_y /= math.sqrt(2)

        self.x += movimento_x
        self.y += movimento_y

        self.x = max(0, min(self.x, self.larghezza_finestra - self.larghezza_sprite))
        self.y = max(0, min(self.y, self.altezza_finestra - self.altezza_sprite))

        tempo_attuale = pygame.time.get_ticks()
        if tempo_attuale - self.tempo_ultimo_frame > self.tempo_frame:
            self.frame_attuale = (self.frame_attuale + 1) % len(self.direzioni[self.direzione_corrente])
            self.tempo_ultimo_frame = tempo_attuale
