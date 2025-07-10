
#print("tu nombre y apellido es " + input(" dime tunombre ")+input("dime tu apellido  "))

#hacer un codido que aga 2 preguntas a tu amigo y que el resultado lo muestre  usando saltos de linea

#print("el nombre de tu cerveza \n es   " + input ("que ciudad te gustaria visitar:?")+ input("cual es tu trago preferido")+ "¨´")


#como podemos usar y refactorizar essta funcion 
""""""
def calcular_area_rectangulo(base,altura):#calculo de area de un triangulo  de 2 3 lados diferentes imprimiendo  ressultados de formasimilar 
    return base * altura
def mostrar_area_rectangulo(numero,base,altura):
    """muestra el area de un rectangulo con formato"""
    area =calcular_area_rectangulo(base,altura)
    print("el area del rectangulomes es ")

    def main():
        """funcion principal del programa"""
        #ejemplo de uso 
    mostrar_area_rectangulo(1,10,5)

    #puedes probar con mas rectangulos
    mostrar_area_rectangulo(5,6,8)

    if __name__=="__main__":
        main()
        