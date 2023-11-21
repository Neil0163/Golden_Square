from lib.todo_list import *
from lib.todo_task import *

def test_integration():
    list_call = TodoList()

    task_call = Todo("Task 1", False)

    task_call.mark_complete()

    list_call.add(task_call.task, task_call.value)

    assert list_call.complete() == ["Task 1"]