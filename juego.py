import random
import time
import re

posibles_palabras = []
pa = re.compile('^[a-z]+$')
limpiar = lambda: print('\n' * 50)
print('Bienvenido al juego del ahorcado.')
time.sleep(2)

def juego():
    try:
        palabra_oculta = random.choice(posibles_palabras)
        print('La palabara elegida tiene', len(set(palabra_oculta)), 'letras')
        time.sleep(2)
        print('Empezemos el juego.')
        letras_acertada = []
        vidas = 10
        while True:
            while True:
                letra = input('Introduce una letra para adivinar si está en la palabra: ')
                if len(letra) != 1 and letra.isnumeric():
                    print('Introduce solo una letra.')
                    time.sleep(1)
                    break
                if letra in palabra_oculta:
                    print('Has acertado la letra!')
                    letras_acertada.append(letra)
                    break
                vidas -= 1
                print('No has acertado la letra')
                print(f'Te queda {vidas} vidas.')
                break
            if vidas == 0:
                print('No te quedan vidas, has perdido. La palabra era', palabra_oculta)
                time.sleep(2)
                break

            estado_actual = ''
            for p in palabra_oculta:
                if p in letras_acertada:
                    estado_actual = estado_actual + p
                else:
                    estado_actual = estado_actual + '_'

            if estado_actual == palabra_oculta:
                print(f'Enhorabuena has ganado! La palabra oculta era {palabra_oculta}')
                time.sleep(3)
                print('\n' * 30)
                break

            print(estado_actual)
            print()
            time.sleep(1)
        return limpiar
    except IndexError:
        print('No se han cargado las palabras para jugar.')
        print()
        time.sleep(2)


def palabras():
    print('¿Qué palabra desea añadir al juego?')
    palabra_nueva = input()
    comprobacion = re.match(pa, palabra_nueva)
    if comprobacion is None:
        print('ERROR. Has intentado introducir un caracter que no \
            es alfabético. Solo se admiten carácteres alfabéticos.')
        time.sleep(1)
    else:
        with open('palabras_juego.txt', 'a') as palabras_juego:

            print(palabra_nueva, file=palabras_juego)


def cargar_palabras():
    with open('palabras_juego.txt', 'r') as archivo:
        carga = archivo.read().split('\n')
    print(carga)
    for x in carga:
        if x not in ('', ' '):
            posibles_palabras.append(x)
            if x not in carga:
                posibles_palabras.append(x)
    print('Se han cargado las palabras correctamente. Ahora puede iniciar el juego. ')


def menu():
    while True:
        print('''¿Qué desea hacer?
                    J -> Jugar
                    A -> Añadir nueva palabra
                    C -> Cargar las palabra al juego
                    S -> Salir''')
        opci = input().lower()

        if opci == 'j':
            juego()
        elif opci == 'a':
            palabras()
        elif opci == 'c':
            cargar_palabras()
        elif opci == 's':
            break
        else:
            print('No has elegido una opción correcta. Vuelve a intentarlo.')
            time.sleep(1)

menu()
