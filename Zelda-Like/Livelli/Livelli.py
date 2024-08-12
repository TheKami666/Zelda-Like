import pygame
import sys
from dialogo import Dialogo


def carica_tiles(tile_sheet_path, dimensione_tile):
    tile_sheet = pygame.image.load(tile_sheet_path).convert_alpha()
    larghezza_tile, altezza_tile = dimensione_tile
    larghezza_sprite, altezza_sprite = tile_sheet.get_size()

    num_colonne = larghezza_sprite // larghezza_tile
    num_righe = altezza_sprite // altezza_tile

    tiles = []
    for riga in range(num_righe):
        for colonna in range(num_colonne):
            rect = pygame.Rect(colonna * larghezza_tile, riga * altezza_tile, larghezza_tile, altezza_tile)
            tile = tile_sheet.subsurface(rect)
            tiles.append(tile)

    return tiles


class Livello1:
    def __init__(self, larghezza_finestra, altezza_finestra):
        self.larghezza_finestra = larghezza_finestra
        self.altezza_finestra = altezza_finestra
        self.tiles = carica_tiles('gfx/erba_scura.png', (32, 32))
        self.tilesAlberi = carica_tiles('gfx/Treescopia.png', (80, 82))
        self.tilesTerra = carica_tiles('gfx/sentiero.png', (16, 16))
        self.dialogo = Dialogo()  # Aggiungi un'istanza di Dialogo
        self.dialogo_attivo = True  # Indica se il dialogo è attivo
        self.mostra_dialogo = True  # Per assicurarsi che il dialogo venga mostrato solo una volta

        self.mappa_alberi = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 0, 1, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        self.mappa_terra = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        self.sfondo = pygame.Surface((larghezza_finestra, altezza_finestra))
        self.hitbox_alberi = []  # Lista di hitbox degli alberi

        larghezza_mappa_terra = len(self.mappa_terra[0]) * self.tilesTerra[0].get_width()
        altezza_mappa_terra = len(self.mappa_terra) * self.tilesTerra[0].get_height()

        # Calcola l'offset per centrare la mappa di terra
        self.offset_x = 0
        self.offset_y = (altezza_finestra - larghezza_mappa_terra) // 2

        self.crea_sfondo()
        self.crea_oggetti()

        self.fade_surface = pygame.Surface((larghezza_finestra, altezza_finestra))
        self.fade_surface.fill((0, 0, 0))  # Superficie nera
        self.fade_alpha = 255  # Opacità iniziale (completamente opaca)
        self.fade_duration = 2000  # Durata del fade-in in millisecondi
        self.fade_start_time = pygame.time.get_ticks()  # Tempo di inizio del fade-in

    def aggiorna(self, schermo):
        self.disegna(schermo)

        if self.dialogo_attivo and self.mostra_dialogo:
            self.dialogo.stampa(schermo, "HELLO WORLD", 0.1)

    def gestisci_input(self, eventi):
        for evento in eventi:
            if evento.type == pygame.KEYDOWN and self.dialogo_attivo == True and self.mostra_dialogo == True:
                if evento.key == pygame.K_SPACE:
                    self.dialogo_attivo = False
                    self.mostra_dialogo = False


    def crea_sfondo(self):
        tile_larghezza, tile_altezza = self.tiles[0].get_size()
        for y in range(0, self.altezza_finestra, tile_altezza):
            for x in range(0, self.larghezza_finestra, tile_larghezza):
                tile = self.tiles[0]
                self.sfondo.blit(tile, (x, y))

    def crea_oggetti(self):
        scala_terra = 2
        larghezza_tile, altezza_tile = self.tilesTerra[0].get_size()
        for riga in range(len(self.mappa_terra)):
            for colonna in range(len(self.mappa_terra[0])):
                if self.mappa_terra[riga][colonna] == 1:
                    terra = self.tilesTerra[0]
                    larghezza_scalata = larghezza_tile * scala_terra
                    altezza_scalata = altezza_tile * scala_terra
                    terra_scalato = pygame.transform.scale(terra, (larghezza_scalata, altezza_scalata))
                    x = colonna * larghezza_tile
                    y = riga * altezza_tile

                    self.sfondo.blit(terra_scalato, (x + self.offset_x, (y + self.offset_y) + 500))

        scala = 2
        larghezza_tile, altezza_tile = self.tilesAlberi[0].get_size()
        for riga in range(len(self.mappa_alberi)):
            for colonna in range(len(self.mappa_alberi[0])):
                if self.mappa_alberi[riga][colonna] == 1:
                    albero = self.tilesAlberi[1]
                    larghezza_scalata = larghezza_tile * scala
                    altezza_scalata = altezza_tile * scala
                    albero_scalato = pygame.transform.scale(albero, (larghezza_scalata, altezza_scalata))

                    x = colonna * larghezza_tile
                    y = riga * altezza_tile
                    self.sfondo.blit(albero_scalato, (x, y))

                    hitbox_x = x
                    hitbox_y = y
                    hitbox_larghezza = larghezza_scalata
                    hitbox_altezza = altezza_scalata

                    hitbox_albero = pygame.Rect(
                        hitbox_x - 2.5,  # Sposta la hitbox a sinistra di 2.5 pixel
                        hitbox_y,  # Mantieni la stessa posizione verticale
                        hitbox_larghezza - 5,  # Riduci la larghezza della hitbox di 5 pixel
                        hitbox_altezza - 25  # Riduci l'altezza della hitbox di 25 pixel
                    )

                    self.hitbox_alberi.append(hitbox_albero)
                    pygame.draw.rect(self.sfondo, (255, 0, 0), hitbox_albero, 2)  # Colore rosso per la hitbox

    def disegna(self, schermo):
        schermo.blit(self.sfondo, (0, 0))

        tempo_attuale = pygame.time.get_ticks()
        tempo_trascorso = tempo_attuale - self.fade_start_time
        if tempo_trascorso < self.fade_duration:
            alpha = int(255 * (1 - (tempo_trascorso / self.fade_duration)))
            self.fade_surface.set_alpha(alpha)
            schermo.blit(self.fade_surface, (0, 0))
        else:
            self.fade_surface.set_alpha(0)  # Assicurati che la superficie sia completamente trasparente dopo il fade-in