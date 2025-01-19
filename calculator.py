import sys
def calculator():
    print("""------------------------------------------------------
                      Choose Any one operation
             ------------------------------------------------------
                      A. Addition 
                      S. Subtraction
                      M. Multiplication
                      D. Division
                      F. Floor division
                      MD. Module division
                      E. Exponentation
                      Ex. Exit
            ----------------------------------------------------------""")

    def addition(a, b):
        return a + b

    def subtraction(a, b):
        return a - b

    def multiplication(a, b):
        return a * b

    def division(a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."

    def floor(a, b):
        return a // b

    def module(a, b):
        return a % b

    def exponentiation(a, b):
        return a ** b

    def exit_program():
        print("Thanks for using the program!")
        sys.exit()

    # Get user input for operation choice
    choice = input("Enter Your Choice: ").strip().lower()

    if choice == 'Ex' or choice == 'ex' or choice == 'EX':
        exit_program()

    try:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    if choice == 'A' or choice == 'a':
        print("Addition of {} and {} is {}".format(num1, num2, (addition(num1, num2))))
    elif choice == 'S' or choice == 's':
        print("Subtraction of {} and {} is {}".format(num1, num2, (subtraction(num1, num2))))
    elif choice == 'M' or choice == 'm':
        print("Multiplication of {} and {} is {}".format(num1, num2, (multiplication(num1, num2))))
    elif choice == 'D' or choice == 'd':
        print("Division of {} and {} is {}".format(num1, num2, (division(num1, num2))))
    elif choice == 'F' or choice == 'f':
        print("Floor Division of {} and {} is {}".format(num1, num2, (floor(num1, num2))))
    elif choice == 'MD' or choice == 'md' or choice == 'Md':
        print("Module Division of {} and {} is {}".format(num1, num2, (module(num1, num2))))
    elif choice == 'E' or choice == 'e':
        print("Exponentation of {} and {} is {}".format(num1, num2, (exponentiation(num1, num2))))
    else:
        print("Your choice is wrong -- Please try again!!")


while True:

    calculator()