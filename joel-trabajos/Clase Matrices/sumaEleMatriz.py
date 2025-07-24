#laberintp
matriz=[[0,1,0,1,1],
        [0,1,0,1,1],
        [0,0,0,0,1],
        [1,1,0,0,1],
        [1,1,1,0,0]]
#recorrido

for fila in matriz:
    for elemento in fila:
        if (elemento == 0 and (matriz[fila][elemento+1] == 0 or matriz[fila][elemento-1] == 0 or matriz[fila+1][elemento] == 0 or matriz[fila-1][elemento] == 0)):
                print("camino libre")
                matriz[fila][elemento]= 5
                print("camino libre")                        
        else:         
            print("obstaculo")
            break
            
def sumarMatriz(matriz):
    print(f"suma = {sum([elemento for fila in matriz for elemento in fila])}")

    return sum([elemento for fila in matriz for elemento in fila])
