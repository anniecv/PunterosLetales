
#print("tu nombre y apellido es " + input(" dime tunombre ")+input("dime tu apellido  "))

#hacer un codido que aga 2 preguntas a tu amigo y que el resultado lo muestre  usando saltos de linea

#print("el nombre de tu cerveza \n es   " + input ("que ciudad te gustaria visitar:?")+ input("cual es tu trago preferido")+ "¨´")


#como podemos usar y refactorizar essta funcion 


lista_secreta = [1,2,3,4,5] #lista secreta

print ("bienvaenido al juego de ahorcado ")
print ("debes descubrir que numeros hay en la lista secreta de 5 elementos ")
print ("pero no puedes ver la directamente, en caso de turno puedes hacer una pregunta  en fomra de codido")
print ("ejemplo: len(lista_secreta) o lista_secre")
print ("cuando creas tener la lista completa escribe adivinar")
print (".----------------------------------------------------------------------.")

#buvle de interaccion

while True:
    instrucion= input("<<<<escribe tu instruccion o adivinar>>>>")
    if instrucion.strip().lower()=="adivinar":
        intento=input("escrive tu intento de la lista separada por comas  ")
        try:
            intento_lista =[int(x.strip()) for x in intento.split(",")]
            if intento_lista == lista_secreta:
                print("correcto has descubierto la lista secreta")
                break
            else:
                print("esta no es la lista correcta sigue preguntando ")
        except ValueError:
            print("error asegurrate de escribir solo numeros separados por comas ")
    else:
        try:
            #evalua la instruccion en el contexto de la lista secreta
            resultado=eval(instrucion,{"lista secreta ":lista_secreta})
            print("resultado:", resultado)
        except Exception as e:
            print("error de instruccion:",e)