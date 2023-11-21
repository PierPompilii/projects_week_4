from lib.agenda import Agenda
from lib.agendaentry import AgendaEntry
from lib.task_list import TaskList
from lib.task import Task
from lib.extractphone import ExtractPhone
from lib.readableentry import ReadableEntry

def test_add_experience_and_show_list():
    agenda = Agenda()
    entry_1 = AgendaEntry ("my title 1", "my contents 1")
    entry_2 = AgendaEntry ("my title 2", "my contents 2")
    agenda.add (entry_1)
    agenda.add (entry_2)
    assert agenda.select_all() == [entry_1, entry_2]
    

def test_add_todo_and_show_incomplete():
    task_list = TaskList()
    todo_1 = Task ("my task 1")
    todo_2 = Task ("my task 2")
    task_list.add_task (todo_1)
    task_list.add_task (todo_2)
    assert task_list.incomplete_task ==  [todo_1, todo_2]

def test_mark_complete_one_action():
    task_list = TaskList()
    todo_1 = Task (" my task 1")
    todo_2 = Task ("my task 2")
    task_list.add_task (todo_1)
    task_list.add_task (todo_2)  
    todo_1.mark_complete()
    assert task_list.complete_task() == [todo_1]

def test_find_number_in_agenda():
    agenda = Agenda()
    phone1 = AgendaEntry("numer 1", "07556441111")
    phone2 = AgendaEntry ("number 2", "07334451111")
    agenda.add(phone1)
    agenda.add(phone2)
    extract = ExtractPhone(agenda)
    assert find_number.extract() == ["07556441111", "07334451111"]

def test_readable_entry():
    agenda = Agenda()
    entry_1 = AgendaEntry ("title", "one two three four")
    agenda.add(entry_1)
    readable = ReadableEntry (agenda)
    assert readable.extract (wpm =2, minutes =2) == entry_1
