email = input("introduce tu email: ")
contadorArroba = 0
contadorPunto = 0

for x in email:
    if x == "@":
        contadorArroba=contadorArroba+1
    elif x == ".":
        contadorPunto=contadorPunto+1

if contadorArroba == 1 and (contadorPunto >1 or contadorPunto == 1):
    print("Tu email es correcto")
else:
    print("tu email es incorrecto")