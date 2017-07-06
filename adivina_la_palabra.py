import os
import sys
import getpass

def espacio(cantidad=1):
    print('\n'*cantidad)

clear = lambda: os.system('cls')
while True:
    palabra = getpass.getpass('\nIngrese la palabra a adivinar: ').upper()
    if  not palabra.isalpha():
        print('\n Error:Ingrese solo letras')
        continue
    break
while True:
    try:
        intentos = int(input('Número de intentos fallidos permitidos: '))
        break
    except:
        print('Error: ingrese solo números')
        continue

clear()
espacio(2)
actual = list('_'*len(palabra))
print(' '*10, ' '.join(actual))
espacio(2)


while True:
    if intentos == 0:
        clear()
        print('La palabra era:')
        espacio()
        print(' '*10,' '.join(list(palabra)))
        espacio()
        print('Has perdido \n')
        sys.exit()
        break

    while True:
        letra = input('Ingrese una letra: ').upper()
        if len(letra) != 1:
            print('\nError: Ingrese solo una (1) letra\n')
            continue
        break

    cantidad = palabra.count(letra)

    if letra in palabra:
        posicion = palabra.index(letra)
        izq = len(palabra[:posicion])
        der = len(palabra[posicion+1:])

        if letra in actual:
            clear()
            print('La letra ya se encuentra en la palabra')
            espacio()
            print(' '*10, ' '.join(actual))
            intentos -= 1
            espacio()
            print('Intentos fallidos restantes: ', intentos, '\n')
            continue

        actual[posicion] = letra

        if cantidad is not 1:
            for i in range(cantidad-1):
                posicion = palabra.index(letra, posicion+1)
                izq = len(palabra[:posicion])
                der = len(palabra[posicion+1:])
                actual[posicion] = letra

        if actual.count('_') == 0:
            clear()
            print('La palabra es:')
            espacio()
            print(' '*10,' '.join(actual))
            espacio()
            print('Felicidades! Has ganado\n')
            sys.exit()

        clear()
        espacio(2)
        print(' '*10, ' '.join(actual))
        espacio()
        print('Intentos fallidos restantes: ', intentos)
        espacio()
    else:
        clear()
        print('La letra no se encuentra en la palabra')
        espacio()
        print(' '*10, ' '.join(actual))
        intentos -= 1
        espacio()
        print('Intentos fallidos restantes: ', intentos, '\n')
