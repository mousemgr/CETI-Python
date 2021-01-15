from class_person_module import Persona

while True:

    print("---------- MENU ----------")
    print("1.- Registrar Persona")
    print("2.- Consultar Personas")
    print("3.- Salir")
    opcion = input("Elige una opción:")
    
    if opcion == "1":
        p = Persona()
        p.capturar_informacion()
        p.genera_DNI()
        print("---------- Información Persona ----------")
        print("Peso:" + str(p.calcular_IMC()))
        print("Mayor de Edad:" + str(p.es_mayor_edad()))
        p.imprimir_informacion()
        p.escribir_archivo()
    elif opcion == "2":
        p = Persona()
        p.leer_archivo()
    else:
        break

    