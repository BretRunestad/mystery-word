
from random import choice


def word_pull():
    """Pulls a list of words from the computer's dictionary"""
    with open("/usr/share/dict/words") as file:
        all_words = file.readlines()
    return all_words


def chooser(a_list):
    """Chooses one word from a list of words"""
    chosen_word = choice(a_list)
    return chosen_word


def set_chosen_word_string(chosen_word):
    """Provides a clean, uppper-cased string"""
    cleaned_word = chosen_word[:-1]
    chosen_word_string = cleaned_word.upper()
    return chosen_word_string


def set_chosen_word_list(chosen_word_string):
    """Creates list form of chosen_word_string"""
    chosen_word_list = list(chosen_word_string[:])
    return chosen_word_list


def length_checker(a_string):
    """Determines the length of a string"""
    string_length = len(a_string[:-1])
    return string_length


def easy_sorter(a_list):
    """Sorts the list of all words into words of 4-6 letters"""
    easy_list = [x for x in a_list if len(x) > 4 and len(x) < 8]
    return easy_list


def med_sorter(a_list):
    """Sorts the list of all words into words of 6-10 letters"""
    med_list = [x for x in a_list if len(x) > 6 and len(x) < 12]
    return med_list


def hard_sorter(a_list):
    """Sorts the list of all words into words of 10+ letters"""
    hard_list = [x for x in a_list if len(x) > 10]
    return hard_list


def starting_text_a():
    """Prints first sentence of starting text"""
    a = "Let the Mystery Word game begin!"
    print(a)
    return(a)


def starting_text_b():
    print(
        "Choose: \nE for Easy Mode, \nM for Medium Mode, \nH for Hard Mode")
    game_mode = input("> ")
    game_mode = game_mode.upper()
    return game_mode


def starting_text_c(string_length):
    """Prints second sentence of starting text, reveals how
    many letters are in the word"""
    b = """I have chosen a word at random. It has {} letters.""".format(
        string_length)
    print(b)
    return(b)


def guess_text(counter):
    """Prompts the user to make a guess, informs how
    many guesses are reaining"""
    a = "Make a guess! You have {} left.".format(counter)
    print(a)
    return a


def repeat_guess_check(capsletter, guess_list):
    "Checks to see if the guessed letter has already been guessed"
    if capsletter in guess_list:
        print("""You've already guessed that letter.  Try another.""")
        return "guess again"
    else:
        return "pass"


def error_checking(capsletter):
    """Checks to make sure that the guess is a) not more than one
    letter, and b) a standard letter of the alphabet"""
    if len(capsletter) > 1:
        print("Please guess only one letter.")
        return "not ok"
    elif capsletter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print("Please guess a letter.")
        return "not ok"
    else:
        return "ok"


def append_guess_list(guess, guess_list):
    """Appends the guessed letter to the list of guesses"""
    guess_list.append(guess)
    return guess_list


def success_text():
    """Prints successful guess text"""
    yay = "Good guess!\n"
    print(yay)
    return yay


def failure_text():
    """Prints unsuccessful guess text."""
    nay = "Sorry. Bad guess.\n"
    print(nay)
    return nay


def get_guess():
    """Takes an input from the user and capitalizes it"""
    letter = input("> ")
    capsletter = letter.upper()
    return capsletter


def list_visualizer(chosen_word_list, guess_list):
    """"Takes the list form of the word you're trying to guess and checks
    it against the list of guesses to create a string visualization """
    usage_list = chosen_word_list[:]
    visual_string = ""
    for index, letter in enumerate(usage_list):
        if letter not in guess_list:
            usage_list[index] = "_"
            visual_string = ' '.join(usage_list)
    print(visual_string)
    return visual_string


def guess_checker(a_guess, chosen_word_string, counter):
    """Checks to see whether the guess is part of the chosen word,
    and lowers the counter by one for incorrect guesses"""
    a_guess = a_guess.upper()
    if a_guess in chosen_word_string:
        success_text()
        return counter
    else:
        counter = counter - 1
        failure_text()
        return counter


def win_check(chosen_word_list, guess_list):
    """Tests to see whether all of the letters in the word have been guessed"""
    if all(item in guess_list for item in chosen_word_list):
        return True
    else:
        return False


def lose_check(counter):
    """Tests to see whether the user has run our of guesses"""
    if counter > 0:
        return False
    else:
        return True


def victory_text(chosen_word_string):
    """Prints the winning text, reveals the chosen word"""
    yay = "You win! The word was {}!".format(chosen_word_string)
    print(yay)
    return yay


def loss_text(chosen_word_string):
    """Prints the losing text, reveals the chosen word"""
    nay = "Sorry! You lose. The word was {}.".format(chosen_word_string)
    print(nay)
    return nay


def play_again(end_input):
    if end_input == 'Y':
        pass
    else:
        quit()


if __name__ == "__main__":
    while True:

        starting_text_a()
        game_mode = starting_text_b()
        if game_mode == 'E':
            subset = easy_sorter(word_pull())
            chosen_word = chooser(subset)
        elif game_mode == 'M':
            subset = med_sorter(word_pull())
            chosen_word = chooser(subset)
        elif game_mode == 'H':
            subset = hard_sorter(word_pull())
            chosen_word = chooser(subset)
        else:
            print("If you can't follow directions, you can't play.")
            quit()

        chosen_word_string = set_chosen_word_string(chosen_word)
        chosen_word_list = set_chosen_word_list(chosen_word_string)
        chosen_word_length = length_checker(chosen_word)
        cwl = chosen_word_list[:]

        counter = 8
        guess_list = []

        starting_text_c(chosen_word_length)
        list_visualizer(chosen_word_list, guess_list)

        while counter > 0:
            guess_text(counter)
            capsletter = get_guess()
            while error_checking(capsletter) == "not ok":
                capsletter = get_guess()
            while repeat_guess_check(capsletter, guess_list) == "guess again":
                capsletter = get_guess()
            guess_list = append_guess_list(capsletter, guess_list)
            list_visualizer(chosen_word_list, guess_list)
            counter = guess_checker(capsletter, chosen_word_string, counter)

            x = win_check(chosen_word_list, guess_list)
            if x is True:
                victory_text(chosen_word_string)
                break

        else:
            loss_text(chosen_word_string)
        print("""Would you like to play again?\n If so, type Y""")
        end_input = input("> ")
        end_input = end_input.upper()
        play_again(end_input)
