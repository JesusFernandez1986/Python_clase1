print("Hi, welcome to my game")
numero = input("Enter a number between 1 and 100: ")
numero = int(numero)
tres = 0
cinco = 0

for x in range(100-numero):
    tres = numero % 3
    cinco = numero % 5
    if cinco == 0 and tres == 0:
        print("fizzbuzz")
    elif cinco == 0:
        print("buzz")
    elif tres == 0:
        print("fizz")
    else:
        print(numero)
    numero+=1

