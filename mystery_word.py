from random import choice

with open("/usr/share/dict/words") as file:
    all_words = file.readlines()


def chooser(a_list):
    chosen_word = choice(a_list)
    return chosen_word

#print(chooser(all_words))

def counter(a_string):
    string_length = len(a_string)
    return string_length

def word_interface(string_length):
    return "_ " * string_length

def starting_text(string_length):
    print("Let the Mystery Word game begin!")
    print("I have chosen a word at random. It has {} letters.".format(string_length))
    print(word_interface(string_length))

def guess_text(counter_int):
    return print("Make a guess! You have {} left.".format(counter_int))

def success_text():
    print("Good guess!")

def failure_text():
    print("Sorry. You now have one less guess.")

def get_input():
    input("> ")

def guess_checker(a_guess):
    a_guess = a_guess.upper()
    if a_guess in chooser():
        return True
    else:
        counter -= 1
        return False

chosen_word = chooser(all_words)
string_length = counter(chosen_word)
blank_dashes = word_interface(string_length)
