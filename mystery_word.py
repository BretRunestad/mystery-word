
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

def set_chosen_word_list(chosen_word_string):
    chosen_word_list = list(chosen_word_string[:-1])
    return chosen_word_list

def length_checker(a_string):
    string_length = len(a_string[:-1])
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

def repeat_guess_check(capsletter, guess_list):
    if capsletter in guess_list:
        print ("""You've already guessed that letter.  Try another.""")
        return "guess again"
    else:
        return "pass"

def append_guess_list(guess, guess_list):
    guess_list.append(guess)
    return guess_list

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
    return capsletter

def list_visualizer(chosen_word_list, guess_list):
    """"Takes the list form of the word you're trying to guess and checks
    it against the list of guesses to create a string visualization """
    usage_list = chosen_word_list[:]
    for index, letter in enumerate(usage_list):
        if letter not in guess_list:
            usage_list[index] = "_"
            visual_string = ' '.join(usage_list)
    print(visual_string)
    return visual_string

def guess_checker(a_guess, chosen_word_string, counter):
    a_guess = a_guess.upper()
    if a_guess in chosen_word_string:
        success_text()
        return counter
    else:
        counter = counter - 1
        failure_text()
        return counter

def win_check(chosen_word_list, guess_list):
    if all(item in guess_list for item in chosen_word_list):
        return True
    else:
        return False

def lose_check(counter):
    if counter > 0:
        return False
    else:
        return True

def victory_text(chosen_word_string):
    yay = "You win! The word was {}!".format(chosen_word_string)
    print(yay)
    return yay

def loss_text(chosen_word_string):
    nay = "Sorry! You lose. The word was {}.".format(chosen_word_string)
    print(nay)
    return nay

if __name__ == "__main__":
    chosen_word = chooser(word_pull())
    #Setting global variables for the program:
    chosen_word_string = set_chosen_word_string(chosen_word)
    chosen_word_list = set_chosen_word_list(chosen_word_string)
    print(chosen_word_list)
    chosen_word_length = length_checker(chosen_word)
    cwl = chosen_word_list[:]

    #print(chosen_word_list)
    #print(chosen_word_string)

    counter = 8
    guess_list = []

    starting_text_a()
    starting_text_b(chosen_word_length)
    list_visualizer(chosen_word_list, guess_list)

    while counter > 0:
        guess_text(counter)
        capsletter = get_guess()
        while repeat_guess_check(capsletter, guess_list) == "guess again":
            capsletter = get_guess()
        guess_list = append_guess_list(capsletter, guess_list)
        #print(chosen_word_string)
        #print(chosen_word_list)
        #print(guess_list)
        list_visualizer(chosen_word_list, guess_list)
        counter = guess_checker(capsletter, chosen_word_string, counter)
        #print(counter)

        #print(chosen_word_list)
        #print(guess_list)


        x = win_check(chosen_word_list, guess_list)
        #if x == True:
            #victory_text(chosen_word_string)
            #quit()

    else:
        loss_text(chosen_word_string)
