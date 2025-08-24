 


print("1. Addition of two numbers")
print("2. Subtraction of two numbers")
print("3. Multiplication of two numbers")
print("4. Modulus of two numbers")
print("5. Division of two numbers")
choice = int(input("Enter the choice: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

match choice:
    case 1:
        c = a + b
        print("Addition of two numbers is", c)

    case 2:
        c = a - b
        print("Subtraction of two numbers is", c)

    case 3:
        c = a * b
        print("Multiplication of two numbers is", c)

    case 4:
        c = a % b
        print("Modulus of two numbers is", c)

    case 5:
        c = a / b      
        print("Division of two numbers is", c)

    case _:
        print("Invalid choice!")


