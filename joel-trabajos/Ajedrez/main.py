import pygame
from game_logic import EstadoJuego
from ui import InterfazUsuario
from error_handler import ErrorHandler

def main():
    # Inicializar Pygame
    pygame.init()
    
    # Crear componentes
    ui = InterfazUsuario()
    juego = EstadoJuego()
    error_handler = ErrorHandler()
    clock = pygame.time.Clock()
    
    # Bucle principal
    running = True
    while running:
        # Manejar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if juego.finalizado:
                    juego.reiniciar()
                    error_handler.mostrar_mensaje = False
                else:
                    fila, col = ui.obtener_casilla(evento.pos)
                    
                    if juego.seleccionada is None:
                        pieza = juego.tablero[fila][col]
                        if pieza != ' ':
                            # Verificar turno correcto
                            if (juego.turno == 'blanco' and pieza.isupper()) or \
                               (juego.turno == 'negro' and pieza.islower()):
                                # Durante jaque, solo permitir seleccionar piezas que puedan proteger al rey
                                if juego.jaque:
                                    movimientos_posibles = juego.obtener_movimientos_validos(fila, col)
                                    if movimientos_posibles:
                                        juego.seleccionada = (fila, col)
                                        juego.movimientos_validos = movimientos_posibles
                                    else:
                                        error_handler.mostrar_error("Esta pieza no puede proteger al rey")
                                else:
                                    juego.seleccionada = (fila, col)
                                    juego.movimientos_validos = juego.obtener_movimientos_validos(fila, col)
                                    
                                    # Mostrar error si no hay movimientos válidos
                                    if not juego.movimientos_validos:
                                        error_handler.mostrar_error("No hay movimientos válidos")
                                        juego.seleccionada = None
                    else:
                        # Si hace clic en la misma pieza, deseleccionar
                        if (fila, col) == juego.seleccionada:
                            juego.seleccionada = None
                            juego.movimientos_validos = []
                        # Si hace clic en un movimiento válido
                        elif (fila, col) in juego.movimientos_validos:
                            juego.mover_pieza(juego.seleccionada, (fila, col))
                            juego.seleccionada = None
                            juego.movimientos_validos = []
                        # Si hace clic en otra pieza
                        else:
                            pieza = juego.tablero[fila][col]
                            if pieza != ' ':
                                # Verificar turno correcto
                                if (juego.turno == 'blanco' and pieza.isupper()) or \
                                   (juego.turno == 'negro' and pieza.islower()):
                                    # Durante jaque, solo permitir seleccionar piezas que puedan proteger al rey
                                    if juego.jaque:
                                        movimientos_posibles = juego.obtener_movimientos_validos(fila, col)
                                        if movimientos_posibles:
                                            juego.seleccionada = (fila, col)
                                            juego.movimientos_validos = movimientos_posibles
                                        else:
                                            error_handler.mostrar_error("Esta pieza no puede proteger al rey")
                                    else:
                                        juego.seleccionada = (fila, col)
                                        juego.movimientos_validos = juego.obtener_movimientos_validos(fila, col)
                                        
                                        # Mostrar error si no hay movimientos válidos
                                        if not juego.movimientos_validos:
                                            error_handler.mostrar_error("No hay movimientos válidos")
                                            juego.seleccionada = None
                            else:
                                juego.seleccionada = None
                                juego.movimientos_validos = []
            
            # Reiniciar con la tecla R
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                juego.reiniciar()
                error_handler.mostrar_mensaje = False
        
        # Dibujar
        ui.dibujar_tablero(juego)
        error_handler.dibujar(ui.ventana, juego)
        
        if juego.finalizado:
            error_handler.mostrar_fin_juego(ui.ventana, juego.mensaje)
        
        # Actualizar pantalla
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()