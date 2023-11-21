from lib.todo import Todo


"""of one actions that are in the todo list
    I would like to mark complete that action
    """
    
def test_mark_complete_one_action():
    task1 = Todo("Walk the dog")
    assert task1.complete == False
    task1.mark_complete()
    assert task1.complete == True
    
    