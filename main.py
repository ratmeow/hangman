from const import START_TEXT
from hangman import Hangman


if __name__ == "__main__":
    game = Hangman()

    while True:
        try:
            game_flag = int(input(START_TEXT))
        except ValueError:
            print("Можно вводить только числа")
            print("Попробуйте еще раз")
            continue
        if game_flag == 1:
            game.start_game()
        elif game_flag == 0:
            break
        else:
            print("Недопустимая команда. Список возможных команд [0, 1]")
            print("Попробуйте еще раз")
