num1= 20
num2 = 4

print("suma: ",(num1 + num2))
print("resta: ",(num1 - num2))
print("multiplicasion: ",(num1 * num2))
print("division: ",(num1 / num2))
print("division Exacta: ",(num1 // num2))
print("potencia: ",(num1 ** num2))

# Concatenacion en python

texto1 = "Hola"
texto2 = "Mundo"
textoFinal = texto1 + " " + texto2
print(textoFinal)
print("El saludo es: %s %s" % (texto1, texto2))

saludoFinal = "Saludo: {} {}".format(texto1,texto2)

print(saludoFinal)

saludoFinal2 = "Saludo 2: {x} {y} ".format(x=texto1,y=texto2)
print(saludoFinal2)