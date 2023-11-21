class TaskList():
    def __init__(self):
        self.task_list = []
    
    def add_task (self, task):
        self.task_list.append(task)


    def incomplete_task (self):
        return [task for task in self.task_list if not task.complete]

    def complete_task (self):
        return [task for task in self.task_list if task.complete]
        