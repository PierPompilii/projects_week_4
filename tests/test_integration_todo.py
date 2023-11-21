from lib.todo_list import TodoList
from lib.todo import Todo

"""
    given two todo actions 
    i added those 2 actions
    """
    
def test_add_todo_task():
    todo_list = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Wash dishes")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    assert ["Walk the dog", "Wash dishes"]
    
    """
    given 2 todo actions 
    return those 2 actions as incomplete
    """
    
def test_show_imcomplete_todo_task():
    todo_list = TodoList()
    todo_list.add("Walk the dog")
    todo_list.add("Wash dishes")
    assert todo_list.incomplete() == ["Walk the dog", "Wash dishes"]
    
    '''
    given task that hasent been completed
    show a empty list of completed task
    '''
def test_empty_completed_task():
    todo_list = TodoList()
    todo_list.add("Walk the dog")
    todo_list.add("Wash dishes")
    todo_list.incomplete()== ["Walk the dog", "Wash dishes"]
    assert todo_list.complete() == []
    
    """of two actions that are in the todo list
    I would like to mark complete one of those actions
    """
    
def test_mark_complete_one_action():
    todo_list = TodoList()
    todo_1 = Todo ("Walk the dog")
    todo_2 = Todo ("Wash dishes")
    todo_list.add (todo_1)
    todo_list.add (todo_2)
    todo_1.mark_complete()
    assert todo_list.complete() == [todo_1]
    
    '''
    given two task to be completed
    i decided to quit so i give up al the imcomplete tasks
    '''
def test_too_lazy_to_finish_the_todos():
    todo_list = TodoList()
    todo_list.add("Run")
    todo_list.add("Eat")
    todo_list.give_up() 
    assert todo_list.complete() == ["Run","Eat"]
        
    
        
    
        
        
        
    
    
    
    
