#To make a CALCULATOR and perform basic arithmetic operation with it
#Here along with the basic arithmetic operastions like addition,subtraction,multiplication,division ALSO
#We  added operations like exponenetial,square root and trigo functions in addition to it
import math

def calculator():
    print("Calculator")
    print("Select operation user wants to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (^)")
    print("6. Square Root (√)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("10. Logarithm (log)")

    # To Take input from the user
    choice = input("Enter choice (1-10): ")

    # To Perform the appropriate operation
    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is {result}")
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is {result}")
            else:
                print("Error! Division by zero.")
        elif choice == '5':
            result = num1 ** num2
            print(f"The result of {num1} ^ {num2} is {result}")

    elif choice == '6':
        num = float(input("Enter the number: "))
        if num >= 0:
            result = math.sqrt(num)
            print(f"The square root of {num} is {result}")
        else:
            print("Error! Square root of a negative number.")

    elif choice == '7':
        angle = float(input("Enter the angle in degrees: "))
        result = math.sin(math.radians(angle))
        print(f"The sine of {angle} degrees is {result}")

    elif choice == '8':
        angle = float(input("Enter the angle in degrees: "))
        result = math.cos(math.radians(angle))
        print(f"The cosine of {angle} degrees is {result}")

    elif choice == '9':
        angle = float(input("Enter the angle in degrees: "))
        result = math.tan(math.radians(angle))
        print(f"The tangent of {angle} degrees is {result}")

    elif choice == '10':
        num = float(input("Enter the number: "))
        if num > 0:
            result = math.log(num)
            print(f"The logarithm (base e) of {num} is {result}")
        else:
            print("Error! Logarithm of a non-positive number.")

    else:
        print("Invalid input. Please enter a valid choice.")

# Run the calculator
calculator()
