from lib.find_todo import find_todo
import pytest 

def test_for_todo_in_text():
    result = find_todo("This has #TODO")
    assert result == True 

def test_for_mixed_case_todo_in_text():
    result = find_todo("This is case of #ToDo is mixed")
    assert result == True

def test_for_empty_string_in_text():
    with pytest.raises(Exception) as e:
        find_todo(" ")
    assert str(e.value) == "empty string"
    
def test_multiple_todo_in_text():
    result = find_todo("this case has multiple #TODO, #tOdO #todo")
    assert result == True

