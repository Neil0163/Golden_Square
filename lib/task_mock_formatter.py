class TaskFormatter:
    def __init__(self, tasks): # task is an instance of Task
        self.tasks = tasks 


    def format(self):
        # Returns the task formatted as a string.
        # If the task is not complete, the format is:
        # - [ ] Task title
        # If the task is complete, the format is:
        # - [x] Task title
        formatted_tasks = []
        for title, complete in self.tasks:
            checkbox = "- [ ]" if not complete else "- [x]"
            formatted_task = f"{checkbox} {title}"
            formatted_tasks.append(formatted_task)
        return formatted_tasks