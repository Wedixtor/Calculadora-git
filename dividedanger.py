def dividedanger():
    print('Please enter two numbers to divide.')
    dividend = int(input('Please enter the dividend: '))
    divisor = int(input('Please enter the divisor: '))
    if divisor != 0:
        return(dividend / divisor)
    else:
        return("Division by zero is not allowed.")
