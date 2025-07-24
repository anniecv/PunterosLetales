import copy
from constants import TABLERO_INICIAL

class EstadoJuego:
    def __init__(self):
        self.tablero = copy.deepcopy(TABLERO_INICIAL)
        self.turno = 'blanco'
        self.seleccionada = None
        self.movimientos_validos = []
        self.ultimo_movimiento = None
        self.enroque_disponible = {
            'blanco': {'corto': True, 'largo': True},
            'negro': {'corto': True, 'largo': True}
        }
        self.captura_al_paso = None
        self.jaque = False
        self.finalizado = False
        self.mensaje = ''
        self.rey_blanco = (7, 4)
        self.rey_negro = (0, 4)

    def camino_libre(self, origen, destino):
        fila_or, col_or = origen
        fila_dest, col_dest = destino
        d_f = fila_dest - fila_or
        d_c = col_dest - col_or
        step_f = 0 if d_f == 0 else (1 if d_f > 0 else -1)
        step_c = 0 if d_c == 0 else (1 if d_c > 0 else -1)
        f, c = fila_or + step_f, col_or + step_c
        while (f, c) != (fila_dest, col_dest):
            if self.tablero[f][c] != ' ':
                return False
            f += step_f
            c += step_c
        return True

    def movimiento_valido(self, origen, destino):
        """Verifica si un movimiento respeta las reglas de la pieza y el turno."""
        fo, co = origen
        fd, cd = destino
        pieza = self.tablero[fo][co]
        if pieza == ' ': return False
        if self.turno == 'blanco' and pieza.islower(): return False
        if self.turno == 'negro' and pieza.isupper(): return False

        tipo = pieza.lower()
        d_f, d_c = fd - fo, cd - co

        # Peón
        if tipo == 'p':
            dir_p = -1 if pieza.isupper() else 1
            # avance simple o doble
            if co == cd:
                if d_f == dir_p and self.tablero[fd][cd] == ' ': return True
                if (fo in (1,6)) and d_f == 2*dir_p:
                    if self.tablero[fo + dir_p][co] == ' ' and self.tablero[fd][cd] == ' ':
                        return True
            # captura normal o al paso
            if abs(d_c) == 1 and d_f == dir_p:
                if self.tablero[fd][cd] != ' ' or self.captura_al_paso == (fd, cd):
                    return True
            return False

        # Torre
        if tipo == 'r':
            if (d_f == 0 or d_c == 0) and self.camino_libre(origen, destino):
                return True
            return False

        # Caballo
        if tipo == 'n':
            return (abs(d_f), abs(d_c)) in ((2,1), (1,2))

        # Alfil
        if tipo == 'b':
            if abs(d_f) == abs(d_c) and self.camino_libre(origen, destino):
                return True
            return False

        # Reina
        if tipo == 'q':
            if ((d_f == 0 or d_c == 0) or abs(d_f) == abs(d_c)) and self.camino_libre(origen, destino):
                return True
            return False

        # Rey
        if tipo == 'k':
            # un paso
            if max(abs(d_f), abs(d_c)) == 1:
                return True
            # Enroque
            if d_f == 0 and abs(d_c) == 2:
                lado = 'corto' if d_c > 0 else 'largo'
                if self.enroque_disponible[self.turno][lado]:
                    pasos = [1,2] if lado == 'corto' else [-1,-2,-3]
                    cols = [co + p for p in pasos]
                    # verificar casillas vacías y no en jaque
                    if all(self.tablero[fo][c] == ' ' for c in cols):
                        if not self.esta_en_jaque((fo, co)) and all(
                            not self.esta_en_jaque((fo, co + p)) for p in pasos[:-1]
                        ):
                            return True
            return False

        return False

    def movimiento_deja_jaque(self, origen, destino):
        """Simula el movimiento y verifica si deja al rey en jaque."""
        fo, co = origen
        fd, cd = destino
        pieza_o = self.tablero[fo][co]
        pieza_d = self.tablero[fd][cd]
        rey_backup = (self.rey_blanco, self.rey_negro)

        # ejecutar
        self.tablero[fd][cd] = pieza_o
        self.tablero[fo][co] = ' '
        if pieza_o.lower() == 'k':
            if pieza_o.isupper(): self.rey_blanco = (fd, cd)
            else: self.rey_negro = (fd, cd)

        enjaque = self.esta_en_jaque(
            self.rey_blanco if self.turno == 'blanco' else self.rey_negro
        )
        # restaurar
        self.tablero[fo][co] = pieza_o
        self.tablero[fd][cd] = pieza_d
        self.rey_blanco, self.rey_negro = rey_backup
        return enjaque

    def obtener_movimientos_validos(self, f, c):
        moves = []
        for fd in range(8):
            for cd in range(8):
                if self.movimiento_valido((f, c), (fd, cd)):
                    if not self.movimiento_deja_jaque((f, c), (fd, cd)):
                        moves.append((fd, cd))
        return moves

    def esta_en_jaque(self, posicion_rey):
        """Determina si el rey en posicion_rey está en jaque."""
        for f in range(8):
            for c in range(8):
                p = self.tablero[f][c]
                if p != ' ':
                    defensor = 'blanco' if p.isupper() else 'negro'
                    if defensor != self.turno and self.movimiento_valido((f, c), posicion_rey):
                        return True
        return False

    def es_jaque_mate(self):
        if not self.esta_en_jaque(self.rey_blanco if self.turno == 'blanco' else self.rey_negro):
            return False
        for f in range(8):
            for c in range(8):
                p = self.tablero[f][c]
                if p != ' ' and ((self.turno == 'blanco' and p.isupper()) or (self.turno == 'negro' and p.islower())):
                    if self.obtener_movimientos_validos(f, c):
                        return False
        return True

    def es_ahogado(self):
        if self.esta_en_jaque(self.rey_blanco if self.turno == 'blanco' else self.rey_negro):
            return False
        for f in range(8):
            for c in range(8):
                p = self.tablero[f][c]
                if p != ' ' and ((self.turno == 'blanco' and p.isupper()) or (self.turno == 'negro' and p.islower())):
                    if self.obtener_movimientos_validos(f, c):
                        return False
        return True

    def mover_pieza(self, origen, destino):
        """Realiza el movimiento y actualiza estado: jaque, mate, ahogado, turno."""
        fo, co = origen
        fd, cd = destino
        pieza = self.tablero[fo][co]
        self.ultimo_movimiento = (origen, destino)
        # enroque: mover torre
        if pieza.lower() == 'k' and abs(cd - co) == 2:
            if cd > co:
                self.tablero[fo][5] = self.tablero[fo][7]; self.tablero[fo][7] = ' '
            else:
                self.tablero[fo][3] = self.tablero[fo][0]; self.tablero[fo][0] = ' '
        # mover pieza
        self.tablero[fd][cd] = pieza
        self.tablero[fo][co] = ' '
        # captura al paso
        if pieza.lower() == 'p' and abs(fd - fo) == 2:
            self.captura_al_paso = (fd, cd)
        else:
            self.captura_al_paso = None
        # promoción
        if pieza.lower() == 'p' and fd in (0,7):
            self.tablero[fd][cd] = 'Q' if pieza.isupper() else 'q'
        # actualizar rey
        if pieza.lower() == 'k':
            if pieza.isupper(): self.rey_blanco = (fd, cd)
            else: self.rey_negro = (fd, cd)
            self.enroque_disponible[self.turno] = {'corto': False, 'largo': False}
        # torre afecta enroque
        if pieza.lower() == 'r':
            if self.turno == 'blanco':
                if co == 0: self.enroque_disponible['blanco']['largo'] = False
                if co == 7: self.enroque_disponible['blanco']['corto'] = False
            else:
                if co == 0: self.enroque_disponible['negro']['largo'] = False
                if co == 7: self.enroque_disponible['negro']['corto'] = False
        # cambiar turno
        self.turno = 'negro' if self.turno == 'blanco' else 'blanco'
        # actualizar jaque y estado final
        if self.es_jaque_mate():
            self.jaque = True
            self.finalizado = True
            self.mensaje = f"¡Jaque mate! {'Blancas' if self.turno=='negro' else 'Negras'} ganan"
        elif self.es_ahogado():
            self.jaque = False
            self.finalizado = True
            self.mensaje = "¡Ahogado! Empate"
        elif self.esta_en_jaque(self.rey_blanco if self.turno=='blanco' else self.rey_negro):
            self.jaque = True
            self.mensaje = "¡Jaque!"
        else:
            self.jaque = False
            self.mensaje = ''
        return True

    def reiniciar(self):
        self.__init__()