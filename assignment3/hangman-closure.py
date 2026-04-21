# Task 4
# Hangman game, asks for a secret word, and then asks to guess it letter by letter
# When all letters are guessed, prints a winning message
def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        current_word = [i if i in guesses else " _ " for i in list(secret_word)]  # currently revealed word
        print("".join(current_word))
        return " _ " not in current_word  # returns False until all letters are revealed

    return hangman_closure

word = input("Enter your word: ")
game1 = make_hangman(word)

solved = False
while not solved:
    letter = input("Guess a letter: ")
    solved = game1(letter)

print("Word solved!")
