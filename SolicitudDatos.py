numero_entero = input("Captura un numero entero: ")
numero_entero = int(numero_entero)
numero_decimal = float(input("Captura un numero decimal: "))
nombre = input("Captura tu nombre: ")
suma = numero_entero + numero_decimal
resta = numero_entero - numero_decimal
multiplicacion = numero_entero * numero_decimal
division = numero_entero / numero_decimal

print("Hola " + nombre + ", El resultado de la suma entre " + str(numero_entero) + " y " + str(numero_decimal) + " es " + str(suma))
print("Hola " + nombre + ", El resultado de la resta entre " + str(numero_entero) + " y " + str(numero_decimal) + " es " + str(resta))
print("Hola " + nombre + ", El resultado de la multiplicacion entre " + str(numero_entero) + " y " + str(numero_decimal) + " es " + str(multiplicacion))
print("Hola " + nombre + ", El resultado de la division entre " + str(numero_entero) + " y " + str(numero_decimal) + " es " + str(division))
