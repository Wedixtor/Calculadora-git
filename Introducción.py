import dividedanger

def Calculadora():
    print("Bienvenido a la Calculadora! \n")
    print("Por favor, Elija una siguiente opcion: \n ")
    seleccion = int(input("1.Suma \n2.Resta\n3.Multiplicacion \n4.Division.\n\nSeleccion: "))

    if seleccion == 1:
        print("Hola")
    elif seleccion == 2:
        print("Hola 2")
    elif seleccion == 3:
        print("Hola 3")
    elif seleccion == 4:
        dividedanger.dividedanger()
    else:
        Calculadora()

Calculadora()

