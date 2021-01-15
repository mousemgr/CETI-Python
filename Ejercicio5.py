peso_usuario = float(input("Cuantos kilos pesas: "))
altura_usuario = float(input("Cuantos metros mides: "))

imc = round(peso_usuario / altura_usuario ** 2,2)

if imc < 16:
    print("Criterio de ingreso en hospital")
    print("Valor IMC" + str(imc))
elif imc >= 16 and imc <= 17:
    print("Infrapeso")
    print("Valor IMC" + str(imc))
elif imc > 17 and imc <= 18:
    print("Bajo Peso")
    print("Valor IMC" + str(imc))
elif imc > 18 and imc <= 25:
    print("Peso Normal (Saludable)")
    print("Valor IMC" + str(imc))
elif imc > 25 and imc <= 30:
    print("Sobrepeso (Obesidad de grado I)")
    print("Valor IMC" + str(imc))
elif imc > 30 and imc <= 35:
    print("Sobrepeso Cronico (Obesidad de grado II)")
    print("Valor IMC" + str(imc))
elif imc > 35 and imc <= 40:
    print("Obesidad Premorbida (Obesidad de grado III)")
    print("Valor IMC" + str(imc))
else:
    imc > 40
    print("Obesidad Morbida (Obesidad de grado IV)")
    print("Valor IMC" + str(imc))