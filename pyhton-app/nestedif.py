num = int(input("Enter the Positive number : "))
if num%15==0:
    print("The number is divisible by 15")
else:
    if num%3==0 or num%5==0:
        print("The Number is divisible by 5 or 3")
    else:
        print("Number is neither divisible by 5 or 3")
