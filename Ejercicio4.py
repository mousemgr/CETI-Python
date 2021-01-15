horas_trabajadas = int(input("Cuantas horas trabajaste: "))

if horas_trabajadas <= 40:
    salario = horas_trabajadas * 16
    print("Tu salario es " + str(salario))
else:
    diferencia = horas_trabajadas - 40
    extra = diferencia * 20
    salario = 40 * 16
    salario_total = extra + salario
    print("Tu salario es " + str(salario_total))
