from unittest.mock import Mock
from lib.task_mock_formatter import TaskFormatter

#Mock test for empty list 
# create the function
def test_initially_empty_task_list_mock():
# create the mock variable
    task_formatter = Mock()
# convert the new variable using the method your testing and the intended result
    task_formatter.format.return_value = []
# call the variable
    formatted_task = task_formatter.format()
# return the variable to be tested
    assert formatted_task == []
    
#Mock test for incomplete task
def test_for_incomplete_task_mock():
    mock_task_formatter = Mock()
    mock_task_formatter.format.return_value = ["- [ ] Title"]
    tasks = [("Title", False)]
    formatted_tasks = mock_task_formatter.format()
    assert formatted_tasks == ["- [ ] Title"]
    
def test_format_completed_task():
    mock_task_formatter = Mock()
    mock_task_formatter.format.return_value =["- [x] Title"]
    tasks = [("Title", True)]
    formatted_tasks = mock_task_formatter.format()
    assert formatted_tasks == ["- [x] Title"]
    
    