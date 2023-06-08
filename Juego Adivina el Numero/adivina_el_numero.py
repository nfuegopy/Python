from random import randint
intentos = 0
numero_secreto = randint(1, 100)
nombre = input("Dime tu nombre: ")
print(f"Bueno {nombre}, he pensado un numero entre 1 y 1oo\nTienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input("Cual es el numero: "))
    intentos += 1

    if estimado < numero_secreto:
        print("Mi numero es mas alto")

    if estimado > numero_secreto:
        print("Mi numero es mas bajo")
    if estimado == numero_secreto:
        print(f"Felicitaciones{nombre}! Has adivinado en {intentos} intentos")
        break
if estimado != numero_secreto:
    print(f"Lo siento, no has adivinado, El numero secreo era {numero_secreto}")
