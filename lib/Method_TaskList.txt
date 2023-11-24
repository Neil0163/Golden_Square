
class TaskList():
    def __init__(self):
        self.tasks = []
        
    def add_a_task(self, task):
        # parameters:
        # entry : instance of the class
        # Side effects:
        # Adds a task to an empty list
        self.tasks.append(task)
        
    def list_incomplete(self):
        # returns: 
        # a list of incomplete task entires 
        return [task for task in self.tasks if task.complete == False]
                
    
    def list_complete(self):
        # returns: 
        # a list of complete task entires 
        return [task for task in self.tasks if task.complete == True]