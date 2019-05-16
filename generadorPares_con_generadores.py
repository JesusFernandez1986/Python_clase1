def generadorPares(limite):
    num = 1

    while num<limite:
         yield  num*2
         num+=1

devuelvePares = generadorPares(10)

for x in devuelvePares:
    print(x)

