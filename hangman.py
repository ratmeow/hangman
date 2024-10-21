import random
from const import HANGMAN_PICS


class Hangman:
    def __init__(self):
        self.corpus = self._load_corpus()
        self.pics = HANGMAN_PICS

    @staticmethod
    def _load_corpus():
        with open("words.txt", "r", encoding="utf-8") as f:
            words = f.read().strip().split("\n")
            return words

    def _generate_word(self) -> list[str]:
        if len(self.corpus) == 0:
            return []
        index = random.randint(0, len(self.corpus) - 1)
        return list(self.corpus.pop(index))

    def _init_session(self) -> bool:
        self.error_counter = 0
        self.error_letters = []
        self.word: list[str] = self._generate_word()
        if len(self.word) == 0:
            print("К сожалению вы разгадали все слова в словаре")
            return False
        self.user_word: list[str] = ["_"] * len(self.word)

        return True

    @staticmethod
    def _input_letter() -> str:
        while True:
            letter = input("Введите букву: ").lower()
            if len(letter) > 1:
                print("Нельзя вводить несколько букв.")
                print("Пожалуйста, убедитесь, что вы ввели букву без пробелов и знаков препинания")
                print("Попробуйте еще раз!")
                continue
            if not letter.isalpha():
                print("Нельзя вводить, что-либо кроме букв")
                print("Попробуйте еще раз!")
                continue
            if not 'а' <= letter <= 'я' and letter != "ё":
                print("Данная игра предназначена только для русского языка")
                print("Попробуйте еще раз!")
                continue

            return letter

    def _set_letter(self, user_letter: str):
        if user_letter in self.word:
            positions = [i for i, letter in enumerate(self.word) if letter == user_letter]
            for i in positions:
                self.user_word[i] = user_letter
        elif user_letter not in self.error_letters:
            self.error_counter += 1
            self.error_letters.append(user_letter)

    def _print_current_state(self, current_letter):
        print("Слово: " + "".join(self.user_word))
        print(f"Ошибки ({self.error_counter}): {self.error_letters}")
        print("Буква:", current_letter)
        print(self.pics[self.error_counter])

    def start_game(self):
        print("Загадываю слово...")
        if self._init_session():
            print("Слово загадано")
            while True:
                letter = self._input_letter()
                self._set_letter(letter)
                self._print_current_state(current_letter=letter)
                if self.error_counter == 6:
                    print("Вы проиграли :(")
                    print(f"Загаданное слово: {''.join(self.word)}")
                    break
                if "_" not in self.user_word:
                    print("Поздравляю, вы разгадали слово!")
                    break
