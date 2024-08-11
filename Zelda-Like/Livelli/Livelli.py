import pygame


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
        self.tiles = carica_tiles('gfx/Overworld.png', (8, 8))
        self.tilesAlberi = carica_tiles('gfx/Trees+.png', (32, 32))

        self.sfondo = pygame.Surface((larghezza_finestra, altezza_finestra))

        self.crea_sfondo()

    def crea_sfondo(self):
        tile_larghezza, tile_altezza = self.tiles[0].get_size()
        for y in range(0, self.altezza_finestra, tile_altezza):
            for x in range(0, self.larghezza_finestra, tile_larghezza):
                tile = self.tiles[0]  # Usa il primo tile per l'esempio
                self.sfondo.blit(tile, (x, y))

    def posiziona_alberi(self):
        pass

    def disegna(self, schermo):
        schermo.blit(self.sfondo, (0, 0))
