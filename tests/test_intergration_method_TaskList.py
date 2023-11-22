from lib.Method_TaskList import TaskList
from lib.Method_Task import Task


def test_when_i_add_a_task_it_comes_back_in_incomplete_list():
    tracker = TaskList()
    task_1 = Task("Go and get the shopping")
    task_2 = Task("Wash the car")
    tracker.add_a_task(task_1)
    tracker.add_a_task(task_2)
    assert tracker.list_incomplete() == [task_1, task_2]
    
def test_mark_a_test_as_complete():
    tracker = TaskList()
    task_1 = Task("Go and get the shopping")
    task_2 = Task("Wash the car")
    tracker.add_a_task(task_1)
    tracker.add_a_task(task_2)
    task_1.mark_complete()
    assert tracker.list_incomplete() == [task_2]

def test_for_complete_added_to_list():
    tracker = TaskList()
    task_1 = Task("Go and get the shopping")
    task_2 = Task("Wash the car")
    tracker.add_a_task(task_1)
    tracker.add_a_task(task_2)
    task_1.mark_complete()
    assert tracker.list_complete() == [task_1]
    