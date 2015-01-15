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

def guess_checker(a_guess):
    return True
