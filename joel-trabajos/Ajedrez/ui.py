import pygame
import os
from constants import *

class InterfazUsuario:
    def __init__(self):
        # Inicializar Pygame y crear ventana
        pygame.init()
        self.ventana = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Ajedrez en Python")

        # Cargar imágenes de piezas
        self.imagenes = {}
        self.cargar_imagenes()

        # Fuentes
        self.fuente_texto = pygame.font.SysFont('Arial', 24)
        self.fuente_mensaje = pygame.font.SysFont('Arial', 36, bold=True)

    def cargar_imagenes(self):
        """Carga las imágenes de las piezas desde la carpeta 'pieces'"""
        ruta = os.path.join(os.path.dirname(__file__), "pieces")
        nombres = {
            'p': 'PawnBlack.png', 'P': 'PawnWhite.png',
            'r': 'RookBlack.png', 'R': 'RookWhite.png',
            'n': 'KnightBlack.png', 'N': 'KnightWhite.png',
            'b': 'BishopBlack.png', 'B': 'BishopWhite.png',
            'q': 'QueenBlack.png', 'Q': 'QueenWhite.png',
            'k': 'KingBlack.png', 'K': 'KingWhite.png',
        }

        for codigo, archivo in nombres.items():
            imagen = pygame.image.load(os.path.join(ruta, archivo))
            self.imagenes[codigo] = pygame.transform.scale(imagen, (TAMANO_CASILLA, TAMANO_CASILLA))

    def dibujar_tablero(self, estado_juego):
        """Dibuja todo el tablero y las piezas"""
        self.ventana.fill(BLANCO)

        # 1. Dibujar el patrón de casillas
        for fila in range(8):
            for col in range(8):
                if (fila + col) % 2 == 1:
                    pygame.draw.rect(self.ventana, NEGRO,
                                     (col * TAMANO_CASILLA, fila * TAMANO_CASILLA,
                                      TAMANO_CASILLA, TAMANO_CASILLA))

        # 2. Resaltar selección
        if estado_juego.seleccionada:
            fila, col = estado_juego.seleccionada
            pygame.draw.rect(self.ventana, SELECCION,
                             (col * TAMANO_CASILLA, fila * TAMANO_CASILLA,
                              TAMANO_CASILLA, TAMANO_CASILLA), 4)

        # 3. Dibujar movimientos válidos
        for fila, col in estado_juego.movimientos_validos:
            pygame.draw.circle(self.ventana, MOV_VALIDO,
                               (col * TAMANO_CASILLA + TAMANO_CASILLA // 2,
                                fila * TAMANO_CASILLA + TAMANO_CASILLA // 2),
                               15, 3)

        # 4. Dibujar piezas (usando imágenes)
        for fila in range(8):
            for col in range(8):
                pieza = estado_juego.tablero[fila][col]
                if pieza != ' ' and pieza in self.imagenes:
                    self.ventana.blit(self.imagenes[pieza],
                                      (col * TAMANO_CASILLA, fila * TAMANO_CASILLA))

        # 5. Resaltar rey en jaque
        if estado_juego.jaque:
            if estado_juego.turno == 'blanco':
                fila, col = estado_juego.rey_blanco
            else:
                fila, col = estado_juego.rey_negro

            s = pygame.Surface((TAMANO_CASILLA, TAMANO_CASILLA), pygame.SRCALPHA)
            s.fill((255, 0, 0, 100))  # Rojo semitransparente
            self.ventana.blit(s, (col * TAMANO_CASILLA, fila * TAMANO_CASILLA))

    def obtener_casilla(self, pos):
        """Convierte posición del mouse a coordenadas del tablero"""
        x, y = pos
        fila = y // TAMANO_CASILLA
        col = x // TAMANO_CASILLA
        return fila, col