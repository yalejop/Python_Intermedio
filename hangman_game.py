import os
import random

def read_data():
    data = []
    with open('./archivos/data.txt', 'r', encoding='utf-8') as f:
        list_words = [word.strip().upper() for word in f] #strip function remove the space in the end
        choosen_word = list_words[random.randint(0, len(list_words))]

    return choosen_word

def game(magic_word, letter, game_word):
    if letter in magic_word:
        for i in range(len(magic_word)):
            if letter == magic_word[i]:
                game_word[i] = letter

    return ' '.join(game_word)

    
def run():
    lives = 5
    letter = ''
    magic_word = read_data()
    game_word = ['_' for i in range(len(magic_word))]

    while lives > 0:
        os.system('cls')
        print(f'Vidas restantes: {"❤" * (lives)}')
        print('¡Adivina la palabra!')
        print(game(magic_word, letter, game_word))
        try:
            if len(letter) > 1:
                raise ValueError('Solo puedes ingresar una letra')
            else:
                if game(magic_word, letter, game_word).count('_') > 0:
                    if letter in game(magic_word, letter, game_word):
                        letter = input('Escoge una letra: ').upper()
                    else:
                        lives -= 1
                        if lives > 0:
                            os.system('cls')
                            print(f'Vidas restantes: {"❤" * (lives)}')
                            print('¡Adivina la palabra!')
                            print(game(magic_word, letter, game_word))
                            letter = input('Escoge una letra: ').upper()
                        else:
                            os.system('cls')
                            print('¡Te quedaste sin vidas!\nJuego terminado...\n')
                            print('La palabra era: ' + magic_word)
                else:
                    print('¡Ganaste! √')
                    break

        except ValueError as ve:
            return print(ve)
    

if __name__ == '__main__':
    run()