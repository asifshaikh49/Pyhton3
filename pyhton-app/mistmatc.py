num1 = int(input("Enter the number : "))
num2 = int(input("Enter the number : "))
oprator = input("Enter the Oparator ")
match oprator:
    case "+":
        print("Addtion of two number",num1+num2)
    case "-":
        print("Subtration ",num1-num2)
    case "*":
        print("Multiplication of two number ", num1*num2)
    case "/":
        print("Divsion",num1/num2)
    case _ :
        print("Enter the valid oprator")
