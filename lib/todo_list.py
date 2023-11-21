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
        if self.list_completed == []:
            return self.list_completed
        else:
            return self.list_completed.pop(self.incomplete)

    def give_up(self):
        for todo in self.list_todo:
                todo.mark_complete()
                
                
                