from lib.todo_task import Todo
# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self.taskDict = {}

    def add(self, todo, value=False):
        self.taskDict.update({todo:value})
    def incomplete(self):
        emptyList = []
        for key in self.taskDict:
            if self.taskDict[key] == False:
                emptyList.append(key)
        return emptyList

    def complete(self):
        emptyList = []
        for key in self.taskDict:
            if self.taskDict[key] == True:
                print("This is true")
                emptyList.append(key)
        return emptyList

    def give_up(self):
        for i in self.taskDict:
            self.taskDict.update({i:True})
            

