from lib.todo_list import TodoList
from lib.todo_task import Todo

# First create instances of to-do tasks
task_1 = Todo("Wash the car")
task_2 = Todo("Make dinner")
task_3 = Todo("Go to the shops")
task_3.mark_complete()

# Create an instance of TodoList
todo_list = TodoList()

# Add tasks to the TodoList
todo_list.add(task_3)
todo_list.add(task_1)
todo_list.add(task_2)

# Retrieve and print incomplete tasks
incomplete_tasks = todo_list.incomplete()
print("Incomplete Tasks:")
for task in incomplete_tasks:
    print(task.task)
    
# Retrieve and print completed tasks
completed_tasks = todo_list.complete()
print("\nCompleted Tasks:")
for task in completed_tasks:
    print(task.task)
