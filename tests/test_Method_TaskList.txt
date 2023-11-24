from lib.Method_TaskList import TaskList

#initally the incomplete task list will be empty
def test_for_empty_incomplete_list():
    tracker = TaskList()
    assert tracker.list_incomplete() == []
    
#initally the complete task list will be empty
def test_for_empty_complete_list():
    tracker = TaskList()
    assert tracker.list_complete() == [] 
    
    