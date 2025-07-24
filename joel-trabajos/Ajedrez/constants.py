# Dimensiones del tablero y casillas
ANCHO = 640
ALTO = 640
TAMANO_CASILLA = 80

# Colores RGB (sin transparencia)
BLANCO = (240, 217, 181)      # Color para casillas blancas
NEGRO = (181, 136, 99)        # Color para casillas negras
SELECCION = (247, 247, 105)   # Color para casilla seleccionada
MOV_VALIDO = (106, 168, 79)   # Color para movimientos válidos
JAQUE = (220, 60, 60)         # Color para resaltar jaque

# Colores para mensajes e interfaz
TEXTO = (0, 0, 0)             # Color de texto básico
FONDO_MENSAJE = (50, 50, 50)  # Fondo para mensajes
BORDE_MENSAJE = (220, 220, 100) # Borde para mensajes
TEXTO_MENSAJE = (255, 255, 0) # Texto amarillo para mensajes

# Símbolos Unicode para las piezas
PIEZAS = {
    # Piezas negras (minúsculas)
    'r': '♜',  # Torre
    'n': '♞',  # Caballo
    'b': '♝',  # Alfil
    'q': '♛',  # Reina
    'k': '♚',  # Rey
    'p': '♟',  # Peón
    
    # Piezas blancas (mayúsculas)
    'R': '♖',  # Torre
    'N': '♘',  # Caballo
    'B': '♗',  # Alfil
    'Q': '♕',  # Reina
    'K': '♔',  # Rey
    'P': '♙'   # Peón
}

# Configuración inicial del tablero
TABLERO_INICIAL = [
    # Fila 0 (piezas negras)
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    # Fila 1 (peones negros)
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    # Filas 2-5 (vacías)
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    # Fila 6 (peones blancos)
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    # Fila 7 (piezas blancas)
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]