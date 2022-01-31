def factorial(x):
    factorial = 1
    for i in range (1, x+1):
        factorial *= i
        
    return ("The factorial of" + " " + str(x) + " " + "is" + " " + str(factorial))


print(factorial(6))