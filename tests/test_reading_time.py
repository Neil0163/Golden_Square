import pytest 
from lib.reading_time import reading_time


def test_words_read_is_200(): 
    result = reading_time(""" 
    one two three four five six seven eight nine ten""" * 20)
    assert result == 1.0

def test_words_read_is_400():
    result = reading_time("""
    one tow three four five six seven eight nine ten""" * 40)
    assert result == 2.0
    
def test_words_read_is_300():
    result = reading_time("""
    one tow three four five six seven eight nine ten""" * 30)
    assert result == 1.5
    
def test_empty_string_to_raise_error_message():
    with pytest.raises(Exception) as e:
        reading_time(" ")
    error_message = str(e.value)
    assert error_message == "No word read"
    
def test_for_punctuation():
    result = reading_time(""" ! @ ? . """)
    assert result == 0.0