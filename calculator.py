# This print statement shows the different operation options the user can pick from, when using the calculator.  
print("Operation options\n 1. Subtraction\n 2. Addition\n 3. Multiplication\n 4. Division\n 5. Exponentiation")

#This allows the user to enter their option of choice  from the set of options given above.
option = int(input("Enter your selection here: "))

#This allows the user to enter their first and second numbers.
first_number = int(input("Enter the first number:"))
second_number = int(input("Enter the second number:"))

#This function is responsible for subtracting two given numbers.
def subtraction(a, b):
    substract_number = a - b
    return substract_number

#This function is responsible for adding two given numbers.
def addition(x, y):
    add_number = x + y
    return add_number

#This function is responsible for multiplying two given numbers.
def multiplication(x, y):
    multiply_number = x * y
    return multiply_number

#This function is responsible for dividing two given numbers.
def division(a, b):
    divide_number = a / b
    return divide_number

#This function is responsible for doing a repeated multiplication where there is a base and exponent.
def exponentiation(x, y):
    exponent_number = x ** y
    return exponent_number

#This function is responsible of making sure conditions are met and prints out the calculation.
def calculations():
    if option == 1:
        print(f"{first_number} - {second_number} = {subtraction(first_number, second_number)}")
    elif option == 2:
       print(f"{first_number} + {second_number} = {addition(first_number, second_number)}")
    elif option == 3:
       print(f"{first_number} * {second_number} = {multiplication(first_number, second_number)}")
    elif option == 4:
        print(f"{first_number} / {second_number} = {division(first_number, second_number)}")
    elif option == 5:
        print(f"{first_number} ** {second_number} = {exponentiation(first_number,second_number)}")
    else:
        print("Please enter valid numbers: ")


if __name__ == "__main__":
    calculations()

