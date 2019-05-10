number1 = float(input("enter first number: "))
number2 = float(input("enter second number: "))
operation = input("enter operation: ")
resultado_suma = number1+number2
resultado_resta = number1-number2
resultado_mult = number1*number2
resultado_div = number1/number2

if operation == "+" or operation == "plus":
    print("el resultado es: ", resultado_suma)
elif operation == "-" or operation == "minus":
    print("el resultado es: ", resultado_resta)
elif operation == "*" or operation == "multiply":
    print("el resultado es: ", resultado_mult)
elif operation == "/" or operation == "divide":
    print("el resultado es: ", resultado_div)
else:
    print("f@*k off")

