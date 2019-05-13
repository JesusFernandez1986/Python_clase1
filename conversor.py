kilometros = float(0)
millas = float(0)
sino = "si"

print("Hola, este programa sirve para convertir unidades de medidas")

while True:
    if sino == "si":
        kilometros = input("introduce los kilometros: ")
        millas = float(kilometros)* 1.6
        print("El resultado es: " + str(millas))
        sino = input("quiere realizar otra conversion? ")
    else:
        print("Adios")
        break




