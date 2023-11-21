from lib.todo_list import *

def test_incomplete_returns_nothing():
    call = TodoList()
    assert call.incomplete() == []

def test_complete_returns_nothing():
    call = TodoList()
    assert call.complete() == []

def test_incomplete_returns_correct_result():
    call = TodoList()
    call.add("Task 1")
    call.add("Task 2")
    call.add("Task 3")
    call.add("Task 4")
    call.add("Task 5")
    call.add("Task 6")
    assert call.incomplete() == ["Task 1", "Task 2", "Task 3", "Task 4", "Task 5", "Task 6"]


def test_complete_returns_correct_value():
    call = TodoList()
    call.add("Task 1", True)
    call.add("Task 2")
    call.add("Task 3")
    call.add("Task 4", True)
    assert call.complete() == ["Task 1", "Task 4"]
