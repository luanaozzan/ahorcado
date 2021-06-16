import random

hang = ["""
A H O R C A D O - Edicion Frutas

   +---+
   |   |
       |
       |
       |
       |
=========""", """
A H O R C A D O - Edicion Frutas

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
A H O R C A D O - Edicion Frutas

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
A H O R C A D O - Edicion Frutas

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
A H O R C A D O - Edicion Frutas

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
A H O R C A D O - Edicion Frutas

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
A H O R C A D O - Edicion Frutas

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]


def getRandomWord():
    palabras = ['manzana', 'banana', 'mango', 'frutilla', 'naranja', 'uva', 'anana',
             'limon', 'maracuya', 'sandia', 'cereza', 'papaya', 'durazno']

    return random.choice(palabras)


def displayBoard(hang, letrasMal, letrasBien, palabraSecreta):
    print(hang[len(letrasMal)])
    print()

    print('Letras fallidos:', end=' ')
    for letra in letrasMal:
        print(letra, end=' ')
    print("\n")

    blanks = '_' * len(palabraSecreta)

    for i in range(len(palabraSecreta)):  # reemplazo blanks con letras correctas
        if palabraSecreta [i] in letrasBien:
            blanks = blanks[:i] + palabraSecreta[i] + blanks[i+1:]

    for letra in blanks:  # show the secret word with spaces in between each letter
        print(letra, end=' ')
    print("\n")


def getGuess(yaAdivinado):
    while True:
        guess = input('Adivina una letra: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Por favor ingresar una unica letra.')
        elif guess in yaAdivinado:
            print('Ya ingresaste esta letra. Por favor elegir otra.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Por favor que sea una letra.')
        else:
            return guess


def nuevoJuego():
    return input("\nQueres jugar de nuevo? ").lower().startswith('s')


letrasMal = ''
letrasBien = ''
palabraSecreta = getRandomWord()
juegoTerminado = False

while True:
    displayBoard(hang, letrasMal, letrasBien, palabraSecreta)

    guess = getGuess(letrasMal + letrasBien)

    if guess in palabraSecreta:
        letrasBien = letrasBien + guess

        todasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasBien:
                todasLetras = False
                break
        if todasLetras:
            print('\nSi! Tu palabra secreta es "' +
                  palabraSecreta+ '"! Ganaste')
            juegoTerminado = True
    else:
        letrasMal = letrasMal + guess

        if len(letrasMal) == len(hang) - 1:
            displayBoard(hang, letrasMal,
                         letrasBien, palabraSecreta)
            print('No tenes mas intentos!\nDespues de ' + str(len(letrasMal)) + ' intentos fallidos y ' +
                  str(len(letrasBien)) + ' intentos correctos, la palabra es "' + palabraSecreta + '"')
            juegoTerminado = True

    if juegoTerminado:
        if nuevoJuego():
            letrasMal = ''
            letrasBien = ''
            juegoTerminado = False
            palabraSecreta = getRandomWord()
        else:
            break