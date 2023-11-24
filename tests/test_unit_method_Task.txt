
from lib.Method_Task import Task

# Test for title init 
def test_for_title_init():
    task = Task("Go and get the shopping")
    assert task.title == "Go and get the shopping"
    
# the task is initally incomplete 
def test_for_i_initally_incomplete():
    task = Task("Wash the car")
    assert task.complete == False
    
# the task is initally incomplete 
def test_marks_complete():
    task = Task("Wash the car")
    task.mark_complete()
    assert task.complete == True    