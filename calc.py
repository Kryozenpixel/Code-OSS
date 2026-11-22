print("Simple Calculator")

while True:
    try:
        number1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        number2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers only.")
        continue

    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        if number2 == 0:
            print("Cannot divide by zero.")
            continue
        result = number1 / number2
    else:
        print("Unknown operator.")
        continue

    print("Result:", result)

    again = input("Another calculation? (yes/no): ").lower()
    if again != "yes":
        break
