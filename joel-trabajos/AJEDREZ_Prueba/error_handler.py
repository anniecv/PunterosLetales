import pygame
from constants import *

class ErrorHandler:
    def __init__(self):
        self.mensaje = ""
        self.mostrar_mensaje = False
        self.tiempo_inicio = 0
        self.duracion = 2000  # 2 segundos

    def mostrar_error(self, mensaje):
        self.mensaje = mensaje
        self.mostrar_mensaje = True
        self.tiempo_inicio = pygame.time.get_ticks()

    def actualizar(self):
        if self.mostrar_mensaje:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_inicio > self.duracion:
                self.mostrar_mensaje = False

    def dibujar(self, ventana, estado_juego):
        if self.mostrar_mensaje:
            # Crear superficie semitransparente para el mensaje de error
            s = pygame.Surface((WIDTH, 60), pygame.SRCALPHA)
            s.fill((50, 50, 50, 200))
            ventana.blit(s, (0, HEIGHT // 2 - 30))

            # Dibujar texto de error
            fuente = pygame.font.SysFont('Arial', 36)
            texto = fuente.render(self.mensaje, True, (255, 0, 0))
            ventana.blit(texto, (WIDTH // 2 - texto.get_width() // 2, HEIGHT // 2 - texto.get_height() // 2))
        
        # Mostrar mensaje de jaque persistente
        if estado_juego.jaque and not estado_juego.finalizado:
            fuente = pygame.font.SysFont('Arial', 36, bold=True)
            texto = fuente.render("¡JAQUE!", True, (220, 0, 0))
            
            # Fondo para el mensaje de jaque
            pygame.draw.rect(ventana, (255, 255, 200), (WIDTH - texto.get_width() - 20, 10, 
                                                        texto.get_width() + 10, texto.get_height() + 10))
            pygame.draw.rect(ventana, (220, 0, 0), (WIDTH - texto.get_width() - 20, 10, 
                                                    texto.get_width() + 10, texto.get_height() + 10), 3)
            
            ventana.blit(texto, (WIDTH - texto.get_width() - 15, 15))
            
            # Mensaje adicional sobre cómo resolver el jaque
            fuente_info = pygame.font.SysFont('Arial', 20)
            texto_info = fuente_info.render("Debes proteger a tu rey", True, (100, 0, 0))
            ventana.blit(texto_info, (WIDTH - texto_info.get_width() - 15, 55))

    def mostrar_fin_juego(self, ventana, mensaje):
        # Definir colores si no están en constants.py
        FONDO_MENSAJE = (50, 50, 50)  # Color de fondo del mensaje
        BORDE_MENSAJE = (220, 220, 100)  # Color del borde
        TEXTO_MENSAJE = (255, 255, 0)  # Color del texto
        
        # Crear superficie semitransparente
        s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        s.fill((0, 0, 0, 150))
        ventana.blit(s, (0, 0))
        
        # Dibujar cuadro de mensaje
        pygame.draw.rect(ventana, FONDO_MENSAJE, (WIDTH//2-200, HEIGHT//2-50, 400, 100))
        pygame.draw.rect(ventana, BORDE_MENSAJE, (WIDTH//2-200, HEIGHT//2-50, 400, 100), 3)

        # Dibujar texto
        fuente = pygame.font.SysFont('Arial', 36, bold=True)
        texto = fuente.render(mensaje, True, TEXTO_MENSAJE)
        ventana.blit(texto, (WIDTH//2 - texto.get_width()//2, HEIGHT//2 - texto.get_height()//2))
        
        # Instrucciones para reiniciar
        fuente_inst = pygame.font.SysFont('Arial', 24)
        texto_inst = fuente_inst.render("Haz clic para reiniciar o presiona R", True, (200, 200, 200))
        ventana.blit(texto_inst, (WIDTH//2 - texto_inst.get_width()//2, HEIGHT//2 + 40))  # CORRECCIÓN: Quitado paréntesis extra