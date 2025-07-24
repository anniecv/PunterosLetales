import pygame
from game_logic import EstadoJuego
from ui import InterfazUsuario
from error_handler import ErrorHandler

def main():
    pygame.init()
    ui = InterfazUsuario()
    juego = EstadoJuego()
    error_handler = ErrorHandler()
    clock = pygame.time.Clock()
    running = True

    while running:
        ui.dibujar_tablero(juego)
        ui.dibujar_piezas(juego.tablero)
        ui.mostrar_mensaje(juego.mensaje)
        ui.mostrar_boton_reiniciar()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and not juego.finalizado:
                pos = pygame.mouse.get_pos()

                # Verificar botón reiniciar
                if ui.click_en_boton_reiniciar(pos):
                    juego.reiniciar()

                else:
                    casilla = ui.obtener_casilla_click(pos)
                    if juego.seleccionada:
                        movimientos = juego.obtener_movimientos_validos(*juego.seleccionada)
                        if casilla in movimientos:
                            juego.mover_pieza(juego.seleccionada, casilla)
                        juego.seleccionada = None
                    else:
                        f, c = casilla
                        pieza = juego.tablero[f][c]
                        if pieza != ' ':
                            if (juego.turno == 'blanco' and pieza.isupper()) or (juego.turno == 'negro' and pieza.islower()):
                                juego.seleccionada = casilla

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
