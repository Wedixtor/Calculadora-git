# main.py

from Suma import adder
from sustraction import sustraction
from Multiplier import multiplier
from dividedanger import dividedanger
from os import system

def main():
    print("Welcome to the Calculator! \n")
    print("Please choose a following option: \n ")
    seleccion = int(input("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division.\n\nSelection: "))

    if seleccion == 1:
        value1 = int(input('Please enter a number: '))
        value2 = int(input('Please enter another number: '))
        print("The addition of the two numbers is:", adder(value1, value2))
    elif seleccion == 2:
        value1 = int(input('Please enter a number: '))
        value2 = int(input('Please enter another number: '))
        print("The subtraction of the two numbers is:", sustraction(value1, value2))
    elif seleccion == 3:
        value1 = int(input('Please enter a number: '))
        value2 = int(input('Please enter another number: '))
        print("The result of the multiplication is:", multiplier(value1, value2))
    elif seleccion == 4:
        value1 = int(input('Please enter a number: '))
        value2 = int(input('Please enter another number: '))
        try:
            print("The result of the division is:", dividedanger(value1, value2))
        except ValueError as e:
            print(e)
    else:
        print("Invalid selection")
    input("\nPress enter to restart")
    system("cls")
    main()

if __name__ == "__main__":
    main()
