from lib.task_mock_formatter import TaskFormatter

#test for empty list 

def test_initially_empty_task_list():
    task_formatter = TaskFormatter([])
    formatted_tasks = task_formatter.format()
    assert formatted_tasks == []
    
    
def test_for_incomplete_task():
    tasks = [("Title", False)]
    task_formatter = TaskFormatter(tasks)
    formatted_tasks = task_formatter.format()
    assert formatted_tasks == ["- [ ] Title"]
    
def test_format_completed_task():
    tasks = [("Title", True)]
    task_formatter = TaskFormatter(tasks)
    formatted_tasks = task_formatter.format()
    assert formatted_tasks == ["- [x] Title"]
    
    