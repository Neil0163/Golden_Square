from lib.make_snippet import *
import pytest

def test_return_string():
    assert type(make_snippet("String")) == str

def test_returns_string_without_dots_at_end():
    assert make_snippet("String") == "String"

def test_this_string_has_more_than_5_words():
    result = make_snippet("This is a more complex sentence")

    assert result == "This is a more complex..."

def test_throws_error_input_not_string():
    with pytest.raises(Exception) as e:
        make_snippet(1)
    error_message = str(e.value)
    assert error_message == "This is not a string."