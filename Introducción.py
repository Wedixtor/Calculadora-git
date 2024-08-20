import dividedanger
import Multiplier
import sustraction
import Suma
from os import system


def Calculadora():
    print("Welcome to the Calculator! \n")
    print("Please choose a following option: \n ")
    seleccion = int(input("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division.\n\nSelection: "))

    if seleccion == 1:
        print("The addition of the two numbers is:", Suma.adder())
    elif seleccion == 2:
        print("The sustraction of the two numbers is:", sustraction.sustration())
    elif seleccion == 3:
        print("The result of the multiplication is:", Multiplier.multiplier())
    elif seleccion == 4:
        print("The result of the division is:", dividedanger.dividedanger())
    else:
        Calculadora()
    input("\nPress enter to restart")
    system("cls")
    Calculadora()

Calculadora()

