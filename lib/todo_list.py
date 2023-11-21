# File: lib/todo_list.py

class TodoList:
    def __init__(self):
        self.taskDict = {}

    def add(self, todo, value=False):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.taskDict.update({todo:value})
    
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        emptyList = []
        for key in self.taskDict:
            if self.taskDict[key] == False:
                emptyList.append(key)
        return emptyList

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        emptyList = []
        for key in self.taskDict:
            if self.taskDict[key] == True:
                emptyList.append(key)
        return emptyList

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for i in self.taskDict:
            self.taskDict[i] = True
            
            

