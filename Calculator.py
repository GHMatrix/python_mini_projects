# Calculator.py

print("Welcome To Gregory's Simple Calculator")

while True:
    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Get user operation
    print("Select the operation: ")
    print("For addition type (+)")
    print("For subtraction type (-)")
    print("For multiplication type (*)")
    print("For division type (/)")

    operation = input("Enter the operation symbol you want to perform (+, -, *, /): ")

    # Perform the operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Dividing by zero"
    else:
        result = "Invalid Operation"

    # Display result
    print("Result:", result)

    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() != "yes":
        print("Goodbye!!")
        break
