running = True
while running == True:
    operation = input("Enter operation (in lowercase): ")
    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter second number: "))
    if operation == "addition":
        sum = num_1 + num_2
        print("Answer: " + str(sum))
    elif operation == "subtraction":
        difference = num_1 - num_2
        print(difference)
    elif operation == "division":
        if num_2 == 0:
            print("You can't divide by zero")
        else:
            quotient = num_1 / num_2
            print(quotient)
    elif operation == "multiplication":
        product = num_1 * num_2
        print(product)
    elif operation == "exponent":
        power = num_1 ** num_2
        print(power)
    else:
        print("This calculator cannot do that")
    user_continue = input("Do you want to continue (y/n) ")
    if user_continue == "n":
        break