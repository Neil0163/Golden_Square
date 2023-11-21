from lib.todo import *
import pytest

def test_check_returns_string():
    assert type(check_todo("String")) == str

def test_check_no_todo_returns_fail():
    assert check_todo("String") == "#TODO Is not in this string."

def test_check_todo_returns_pass():
    assert check_todo("#TODO_PASS") == "#TODO Is in this string."

def test_return_error_input_int():
    with pytest.raises(Exception) as e:
        check_todo(1)
    message = str(e.value)
    assert message == "You have not entered a string."