import mystery_word as mw

def test_word_chooser():
    lista = ['alpha', 'beta', 'gamma', 'delta']
    assert mw.chooser(lista) in lista

def test_hidden_word_length():
    assert mw.counter("alligator") == 9

def test_word_interface():
    assert mw.word_interface(9) == "_ _ _ _ _ _ _ _ _ "
