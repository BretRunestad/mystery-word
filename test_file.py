import mystery_word as mw


def test_chooser():
    lista = ['alpha', 'beta', 'gamma', 'delta']
    assert mw.chooser(lista) in lista


def test_length_checker():
    assert mw.length_checker("alligator\n") == 9


def test_easy_sorter():
    lista = ['cat\n', 'apple\n', 'bananas\n', 'encyclopedias\n']
    assert mw.easy_sorter(lista) == ['apple\n']


def test_med_sorter():
    lista = ['cat\n', 'apple\n', 'bananas\n', 'encyclopedias\n']
    assert mw.med_sorter(lista) == ['bananas\n']


def test_hard_sorter():
    lista = ['cat\n', 'apple\n', 'bananas\n', 'encyclopedias\n']
    assert mw.hard_sorter(lista) == ['encyclopedias\n']


def test_guess_checker():
    assert mw.guess_checker('A', "APPLE", 8) == 8
    assert mw.guess_checker('B', "APPLE", 8) == 7


def test_append_guess_list():
    guess = 'B'
    glist = ['D', 'C']
    assert mw.append_guess_list(guess, glist) == ['D', 'C', 'B']


def test_list_visualizer():
    lista = ['a', 'p', 'p', 'l', 'e']
    listb = ['p', 'q', 'r', 's', 't']
    listc = ['a', 'p', 'e']
    assert type(mw.list_visualizer(lista, listb)) == str
    assert mw.list_visualizer(lista, listb) == '_ p p _ _'
    assert mw.list_visualizer(lista, listc) == 'a p p _ e'
    assert mw.list_visualizer(lista, []) == '_ _ _ _ _'


def test_set_chosen_word_string():
    word = 'apPle\n'
    assert type(mw.set_chosen_word_string(word)) == str
    assert mw.set_chosen_word_string(word) == "APPLE"


def test_set_chosen_word_list():
    word = 'APPLE'
    assert type(mw.set_chosen_word_list(word)) == list
    assert mw.set_chosen_word_list(word) == ['A', 'P', 'P', 'L', 'E']


def test_starting_text_c():
    assert mw.starting_text_c(5) == (
        "I have chosen a word at random. It has 5 letters.")


def test_guess_text():
    assert mw.guess_text(8) == "Make a guess! You have 8 left."


def test_pretty_guess_list():
    a_list = ['D', 'B', 'A', 'C']
    assert mw.pretty_guess_list(a_list) == "A B C D"


def test_repeat_guess_check():
    guessa = "A"
    guessb = "B"
    guess_list = ['B', 'C', 'D']
    assert mw.repeat_guess_check(guessa, guess_list) == "pass"
    assert mw.repeat_guess_check(guessb, guess_list) == "guess again"


def test_error_checking():
    assert mw.error_checking('1') == "not ok"
    assert mw.error_checking('!') == "not ok"
    assert mw.error_checking('ab') == "not ok"
    assert mw.error_checking('A') == "ok"


def test_win_check():
    lista = ['A', 'P', 'P', 'L', 'E']
    listb = ['A', 'B', 'P', 'Q', 'E', 'L']
    listc = ['Q', 'P']
    assert mw.win_check(lista, listb) is True
    assert mw.win_check(lista, listc) is False


def test_lose_check():
    counter1 = 1
    counter2 = 0
    assert mw.lose_check(counter1) is False
    assert mw.lose_check(counter2) is True


def test_victory_text():
    assert mw.victory_text("APPLE") == "You win! The word was APPLE!"


def test_loss_text():
    assert mw.loss_text("APPLE") == "Sorry! You lose. The word was APPLE."
