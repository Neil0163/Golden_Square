
class Task():
    def __init__(self, title):
        self.title = title
        self.complete = False
        
    def mark_complete(self):
        # side effects :
        # marks the task comeplete 
        self.complete =True 
