import random
import time
import re

posibles_palabras = ['arbol', 'cacahuete', 'piscina', 'cocodrilo',
                     'escritorio', 'automovil', 'serpiente']
pa = re.compile('^[a-z]+$')
limpiar = lambda: print('\n' * 50)
print('Bienvenido al juego del ahorcado.')
time.sleep(2)

def juego():
    palabra_oculta = random.choice(posibles_palabras)
    print('La palabara elegida tiene', len(palabra_oculta), 'letras')
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
        for l in palabra_oculta:
            if l in letras_acertada:
                estado_actual = estado_actual + l
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

def palabras():
    print('¿Qué palabra desea añadir al juego?')
    palabra_nueva = input()
    comprobacion = re.match(pa, palabra_nueva)
    if comprobacion is None:
        print('ERROR. Has intentado introducir un número. Solo se admiten carácteres alfabeticos.')
        time.sleep(1)
    else:
        posibles_palabras.append(palabra_nueva)

def menu():
    while True:
        print('''¿Qué desea hacer?
                    J -> Jugar
                    A -> Añadir nueva palabra
                    S -> Salir''')
        opci = input().lower()

        if opci == 'j':
            juego()
        elif opci == 'a':
            palabras()
        elif opci == 's':
            break
        else:
            print('No has elegido una opción correcta. Vuelve a intentarlo.')
            time.sleep(1)

menu()
