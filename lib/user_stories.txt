# As a user
# So that I can keep track of my tasks
# I want a program that I can add todo tasks to and see a list of them.

class Tracker:
    def __init__(self):
        self.todo = []

    def add(self, task):
        self.todo.append(task)

    def list_items(self):
        return self.todo
    
    # As a user
    # So that I can focus on tasks to complete
    # I want to mark tasks as complete and have them disappear from the list.

    def complete_task(self, task):
        for i in self.todo:
            if i == task:
                self.todo.remove(i)
        