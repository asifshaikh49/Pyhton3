# Simple Calculator without using functions

num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero."
else:
    result = "Invalid operator."

print(f"Result: {result}")

