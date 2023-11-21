from lib.grammar_check import *
import pytest

def test_is_not_string():
    with pytest.raises(Exception) as e:
        verify_grammar(1)
    message = str(e.value)
    assert message == "This is not a string."

def test_first_letter_is_not_uppercase():
    assert verify_grammar("string.") == "Incorrect grammar."

def test_last_letter_is_not_punctuation():
    assert verify_grammar("String") == "Incorrect grammar."

def test_if_no_uppercase_and_no_punctuation():
    assert verify_grammar("string") == "Incorrect grammar."

def test_correct_grammar():
    assert verify_grammar("String.") == "Correct grammar."