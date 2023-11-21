from lib.todo import Todo
class TodoList:
    def __init__(self):
        self.list_todo = []
        self.list_completed = []
        

    def add(self, todo):
        self.list_todo.append(todo)
        
    def incomplete(self):
        return self.list_todo


    def complete(self):
        for todo in self.list_todo:
            if todo.complete is True:
                self.list_completed.append(todo)
                return self.list_completed
            else:
                return []
        
            
    def give_up(self):
        for todo in self.list_todo:
            self.list_completed.append(todo)
            return self.list_completed