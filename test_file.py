import mystery_word as mw


def test_chooser():
    lista = ['alpha', 'beta', 'gamma', 'delta']
    assert mw.chooser(lista) in lista

def test_length_checker():
    assert mw.length_checker("alligator") == 9

def test_guess_checker():
    assert mw.guess_checker('A', "APPLE", 8) == 8
    assert mw.guess_checker('B', "APPLE", 8) == 7

def test_list_visualizer():
    lista = ['a', 'p', 'p', 'l', 'e']
    listb = ['p', 'q', 'r', 's', 't']
    assert type(mw.list_visualizer(lista, listb)) == str
    assert mw.list_visualizer(lista, listb) == '_ p p _ _'
    assert mw.list_visualizer(lista, []) == '_ _ _ _ _'

def test_set_chosen_word_string():
    word = 'apPle'
    assert type(mw.set_chosen_word_string(word)) == str
    assert mw.set_chosen_word_string(word) == "APPLE"

def test_set_chosen_word_list():
    word = 'apPle'
    assert type(mw.set_chosen_word_list(word)) == list
    assert mw.set_chosen_word_list(word) == ['A', 'P', 'P', 'L', 'E']

def test_starting_text_b():
    assert mw.starting_text_b(5) == "I have chosen a word at random. It has 5 letters."

def test_guess_text():
    assert mw.guess_text(8) == "Make a guess! You have 8 left."

def test_win_check():
    lista = ['A', 'P', 'P', 'L', 'E']
    listb = ['A', 'B', 'P', 'Q', 'E', 'L']
    listc = ['Q', 'P']
    assert mw.win_check(lista, listb) == True
    assert mw.win_check(lista, listc) == False

def test_lose_check():
    counter1 = 1
    counter2 = 0
    assert mw.lose_check(counter1) == True
    assert mw.lose_check(counter2) == False

def test_victory_text():
    assert mw.victory_text("APPLE") == "You win! The word was APPLE!"

def test_failure_text():
    assert mw.failure_text("APPLE") == "Sorry! You lose. The word was APPLE."
