import pygame
from constants import WIDTH, HEIGHT, COLORS
import os

class InterfazUsuario:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT + 60))  # espacio extra para texto
        pygame.display.set_caption("Ajedrez")
        self.font = pygame.font.SysFont(None, 36)
        self.boton_reiniciar = pygame.Rect(WIDTH // 2 - 80, HEIGHT + 10, 160, 40)

    def dibujar_tablero(self, juego):
        colores = [COLORS['claro'], COLORS['oscuro']]
        for f in range(8):
            for c in range(8):
                color = colores[(f + c) % 2]
                pygame.draw.rect(self.screen, color, pygame.Rect(c * 80, f * 80, 80, 80))

    def dibujar_piezas(self, tablero):
        for f in range(8):
            for c in range(8):
                pieza = tablero[f][c]
                if pieza != ' ':
                    ruta_base = os.path.dirname(__file__)  # Carpeta donde está ui.py
                    ruta_imagen = os.path.join(ruta_base, "pieces", f"{self.obtener_nombre_archivo(pieza)}.png")
                    imagen = pygame.image.load(ruta_imagen)
                    self.screen.blit(imagen, (c * 80, f * 80))

    def obtener_nombre_archivo(self, pieza):
        nombres = {
            'p': 'PawnBlack', 'r': 'RookBlack', 'n': 'KnightBlack',
            'b': 'BishopBlack', 'q': 'QueenBlack', 'k': 'KingBlack',
            'P': 'PawnWhite', 'R': 'RookWhite', 'N': 'KnightWhite',
            'B': 'BishopWhite', 'Q': 'QueenWhite', 'K': 'KingWhite'
        }
        return nombres.get(pieza, '')

    def obtener_casilla_click(self, pos):
        x, y = pos
        return y // 80, x // 80

    def mostrar_mensaje(self, mensaje):
        pygame.draw.rect(self.screen, (220, 220, 220), (0, HEIGHT, WIDTH, 60))  # fondo claro
        if mensaje:
            texto = self.font.render(mensaje, True, (10, 10, 10))
            self.screen.blit(texto, (20, HEIGHT + 15))

    def mostrar_boton_reiniciar(self):
        pygame.draw.rect(self.screen, (0, 128, 0), self.boton_reiniciar)
        texto = self.font.render("Reiniciar", True, (255, 255, 255))
        self.screen.blit(texto, (self.boton_reiniciar.x + 20, self.boton_reiniciar.y + 5))

    def click_en_boton_reiniciar(self, pos):
        return self.boton_reiniciar.collidepoint(pos)