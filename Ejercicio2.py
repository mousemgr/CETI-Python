
moneda_dcentavos = input("Cuentas monedas tienes de 10 centavos: ")
moneda_dcentavos = int(moneda_dcentavos)
moneda_vcentavos = input("Cuentas monedas tienes de 20 centavos: ")
moneda_vcentavos = int(moneda_vcentavos)
moneda_ccentavos = input("Cuentas monedas tienes de 50 centavos: ")
moneda_ccentavos = int(moneda_ccentavos)
moneda_peso = input("Cuentas monedas tienes de a peso: ")
moneda_peso = int(moneda_peso)
moneda_dos = input("Cuentas monedas tienes de 2 pesos: ")
moneda_dos = int(moneda_dos)
moneda_cinco = input("Cuentas monedas tienes de 5 pesos: ")
moneda_cinco = int(moneda_cinco)
moneda_diez = input("Cuentas monedas tienes de 10 pesos: ")
moneda_diez = int(moneda_diez)

nombre = input("Captura tu nombre: ")

suma_dcentavos = moneda_dcentavos * 0.10
suma_vcentavos = moneda_vcentavos * 0.20
suma_ccentavos = moneda_ccentavos * 0.50
suma_peso = moneda_peso * 1
suma_dos = moneda_dos * 2
suma_cinco = moneda_cinco * 5
suma_diez = moneda_diez * 10
suma = suma_dcentavos + suma_vcentavos + suma_ccentavos + suma_peso + suma_dos + suma_cinco + suma_diez

print("Hola " + nombre + ", tienes " + str(suma))


