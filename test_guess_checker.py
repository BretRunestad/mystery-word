import mystery_word as mw

def test_correct_output():
    booli = mw.guess_checker("")
    assert type(booli) == bool
