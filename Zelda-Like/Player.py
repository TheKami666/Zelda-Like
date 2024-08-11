import pygame
import math

class Player:
    def __init__(self, larghezza_finestra, altezza_finestra, velocita_giocatore):
        self.larghezza_finestra = larghezza_finestra
        self.altezza_finestra = altezza_finestra
        self.velocita = velocita_giocatore
        self.x = larghezza_finestra // 2
        self.y = altezza_finestra // 2
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
            'idle_su': [8],
            'idle_giu': [0],
            'idle_sinistra': [12],
            'idle_destra': [4],
            'su': [8, 9, 10, 11],
            'giu': [0, 1, 2, 3],
            'sinistra': [12, 13, 14, 15],
            'destra': [4, 5, 6, 7]
        }

        self.direzione_corrente = 'idle_giu'
        self.frame_attuale = 0
        self.larghezza_sprite = DIM_FRAME_SPRITE_PG[0] * SCALA
        self.altezza_sprite = DIM_FRAME_SPRITE_PG[1] * SCALA
        self.tempo_ultimo_frame = pygame.time.get_ticks()
        self.tempo_frame = 100
        self.inMovimento = False

        # Definisce una hitbox centrata verticalmente nello sprite
        self.larghezzaHitbox = self.larghezza_sprite  # Puoi regolare la larghezza come desideri
        self.altezzaHitbox = self.altezza_sprite * 0.7  # Puoi regolare l'altezza come desideri
        self.hitbox = pygame.Rect(
            self.x + (self.larghezza_sprite - self.larghezzaHitbox) // 2,
            self.y + (self.altezza_sprite - self.altezzaHitbox) // 2,
            self.larghezzaHitbox,
            self.altezzaHitbox
        )

    def disegna(self, schermo):
        if self.inMovimento:
            frame_index = self.direzioni[self.direzione_corrente][self.frame_attuale]
        else:
            direzione_idle = f'idle_{self.direzione_corrente}'
            frame_index = self.direzioni.get(direzione_idle, [0])[0]

        schermo.blit(self.frames[frame_index], (self.x, self.y))
        self.disegnaHitbox(schermo)

    def disegnaHitbox(self, schermo):
        hitboxColore = (0, 255, 0)
        pygame.draw.rect(schermo, hitboxColore, self.hitbox, 2)

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
            self.inMovimento = True
        elif keys[pygame.K_s]:
            movimento_y += velocita_corrente
            self.direzione_corrente = 'giu'
            self.inMovimento = True
        elif keys[pygame.K_d]:
            movimento_x += velocita_corrente
            self.direzione_corrente = 'destra'
            self.inMovimento = True
        elif keys[pygame.K_w]:
            movimento_y -= velocita_corrente
            self.direzione_corrente = 'su'
            self.inMovimento = True
        else:
            self.inMovimento = False

        if self.inMovimento:
            self.hitbox.x += movimento_x
            self.hitbox.y += movimento_y

        self.hitbox.x = max(0, min(self.hitbox.x, self.larghezza_finestra - self.hitbox.width))
        self.hitbox.y = max(0, min(self.hitbox.y, self.altezza_finestra - self.hitbox.height))

        self.x = self.hitbox.x - (self.larghezza_sprite - self.larghezzaHitbox) // 2
        self.y = self.hitbox.y - (self.altezza_sprite - self.altezzaHitbox) // 2

        # Gestione dell'animazione
        tempo_attuale = pygame.time.get_ticks()
        if tempo_attuale - self.tempo_ultimo_frame > self.tempo_frame:
            if self.inMovimento:
                self.frame_attuale = (self.frame_attuale + 1) % len(self.direzioni[self.direzione_corrente])
            else:
                self.frame_attuale = 0
            self.tempo_ultimo_frame = tempo_attuale

        # Controlla se il giocatore è fermo
        if movimento_x == 0 and movimento_y == 0:
            self.inMovimento = False

    def rileva_collisione(self, altro_rettangolo):
        return self.hitbox.colliderect(altro_rettangolo)
