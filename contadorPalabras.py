nombre="smartninja la mejor escuela de programacion"
contador = 0

for x in nombre:
    if x == " ":
        contador = contador + 0
    else:
        contador+=1

print(contador)