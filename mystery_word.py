
from random import choice

def word_pull():
    with open("/usr/share/dict/words") as file:
        all_words = file.readlines()
    return all_words

def chooser(a_list):
    chosen_word = choice(a_list)
    return chosen_word

def set_chosen_word_string(chosen_word):
    chosen_word_string = chosen_word.upper()
    return chosen_word_string

def set_chosen_word_list(chosen_word):
    chosen_word_upper = chosen_word.upper()
    chosen_word_list = list(chosen_word_upper)
    return chosen_word_list

def length_checker(a_string):
    string_length = len(a_string)
    return string_length

def starting_text_a():
    a= "Let the Mystery Word game begin!"
    print(a)
    return(a)

def starting_text_b(string_length):
    b = "I have chosen a word at random. It has {} letters.".format(string_length)
    print(b)
    return(b)

def guess_text(counter):
    a = "Make a guess! You have {} left.".format(counter)
    print(a)
    return a

def success_text():
    yay = "Good guess!"
    print(yay)
    return yay

def failure_text():
    nay = "Sorry.  You now have one less guess."
    print(nay)
    return nay

def get_guess():
    letter = input("> ")
    capsletter = letter.upper()
    guess_list.append(capsletter)

def list_visualizer(chosen_word_list, guess_list):
    """"Takes the list form of the word you're trying to guess and checks
    it against the list of guesses to create a string visualization """
    for index, letter in enumerate(chosen_word_list):
        if letter not in guess_list:
            chosen_word_list[index] = "_"
            visual_string = ' '.join(chosen_word_list)
    return visual_string

def guess_checker(a_guess, chosen_word_string, counter):
    a_guess = a_guess.upper()
    if a_guess in chosen_word_string:
        return counter
    else:
        counter -= 1
        return counter

def win_check(chosen_word_list, guess_list):
    for word in chosen_word_list:
        if word in guess_list:
            return True
        else:
            return False

def lose_check(counter):
    if counter > 0:
        return True
    else:
        return False

def victory_text(chosen_word_string):
    yay = "You win! The word was {}!".format(chosen_word_string)
    print(yay)
    return yay

def failure_text(chosen_word_string):
    nay = "Sorry! You lose. The word was {}.".format(chosen_word_string)
    print(nay)
    return nay
