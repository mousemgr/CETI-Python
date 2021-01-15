import random

respuesta = -1
piso = 0
techo = 50
intentos_jugador = 1
numero_random = random.randint(1,50)
intentos_totales = 4


print(numero_random)
print("Estoy pensando un numero entre 1 y 50")
while respuesta != numero_random and intentos_jugador<=intentos_totales:
    respuesta = int(input("Intento " + str((intentos_jugador)) + "?"))
    if respuesta == numero_random:
        break
    elif respuesta < numero_random:
        piso = respuesta
    else:
        techo = respuesta
    print("El numero esta entre " + str(piso) + " y " + str(techo))
    intentos_jugador+=1

if intentos_jugador>intentos_totales:
    print("Se acabaron los intentos, el numero que pense era " + str(numero_random))
else:
    print("Felicidades, Ganaste...!!!")

