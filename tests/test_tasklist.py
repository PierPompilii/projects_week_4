from lib.task_list import TaskList

def test_task_list():
    task_list = TaskList()
    assert task_list.incomplete_task() == []