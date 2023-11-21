from lib.task import Task
def test_task():
    entry = Task ("my task 1")
    assert entry.title == "my task 1" 
