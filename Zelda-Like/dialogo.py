import pygame
import time

def carica_immagini_per_caratteri(percorso_immagini, dimensione_scalatura):
    caratteri = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    mappa_caratteri = {}

    for carattere in caratteri:
        try:
            immagine_originale = pygame.image.load(f'{percorso_immagini}/{carattere}.png').convert_alpha()
            larghezza_scalata = immagine_originale.get_width() * dimensione_scalatura
            altezza_scalata = immagine_originale.get_height() * dimensione_scalatura
            immagine_scalata = pygame.transform.scale(immagine_originale, (larghezza_scalata, altezza_scalata))
            mappa_caratteri[carattere] = immagine_scalata
        except FileNotFoundError:
            print(f"Immagine per '{carattere}' non trovata.")

    return mappa_caratteri

class Dialogo:
    def __init__(self):
        self.pathAlfabeto = 'gfx/Font/AlfabetoMaiuscolo'
        self.pathSfondo = 'gfx/Font/fontSfondo.png'
        self.dimensione_scalatura = 2
        self.mappa_caratteri = carica_immagini_per_caratteri(self.pathAlfabeto, self.dimensione_scalatura)
        self.sfondo = pygame.image.load(self.pathSfondo).convert_alpha()
        self.sfondo = pygame.transform.scale(self.sfondo, (800, 100))
        self.indice_carattere = 0
        self.tempo_ultimo_carattere = time.time()
        self.mostrato = False


    def stampa(self, schermo, stringa_da_stampare, ritardo):
        if self.mostrato == True:
            return

        larghezza_schermo = schermo.get_width()
        y = schermo.get_height() - self.sfondo.get_height()
        schermo.blit(self.sfondo, (0, y))  # Disegna lo sfondo

        if time.time() - self.tempo_ultimo_carattere > ritardo:
            if self.indice_carattere < len(stringa_da_stampare):
                self.indice_carattere += 1
                self.tempo_ultimo_carattere = time.time()

        x_pos = (larghezza_schermo - self.calcola_larghezza_testo(stringa_da_stampare)) // 2
        x = 0  # Posizione x per il disegno del testo
        for i in range(self.indice_carattere):
            carattere = stringa_da_stampare[i]
            if carattere in self.mappa_caratteri:
                immagine = self.mappa_caratteri[carattere]
                schermo.blit(immagine, (x + x_pos, y + 10))
                x_pos += immagine.get_width() + 1
            elif carattere == ' ':
                x_pos += 8  # Spazio tra le parole


    def calcola_larghezza_testo(self, stringa_da_stampare):
        larghezza_totale = 0
        for carattere in stringa_da_stampare:
            if carattere in self.mappa_caratteri:
                larghezza_totale += self.mappa_caratteri[carattere].get_width() + 1
            elif carattere == ' ':
                larghezza_totale += 8
        return larghezza_totale

