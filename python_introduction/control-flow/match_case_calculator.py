num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
match operation:
    case "+":
        print("The result is", num1 + num2)
    case "-":
        print("The resut is", num1 - num2)
    case "*":
        print("The result is", num1 * num2)
    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = num1 / num2
        print("The result is", num1 / num2)
    case _:
        print("Invalid operation")
