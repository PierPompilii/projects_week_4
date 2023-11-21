1 - Describe the problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

2 - Design the class system

┌───────────────────────────────────────────────────────┐
│   Agenda                                         │
│                                                       │      ▼
│     record (expiriences)                              │
│     read (experiences)                                │
│     select (expirences)                               │
│     read time (expiriences)                           │
│     see a list (task to do)                           │
│     see a list (contacts)                             │
│                                                       │
│                                                       │
│                                                       │
│                                                       │
│                                                       │
│                                                       │
│                                                       │
└────────────────────────────┬──────────────────────────┘
                             │
                             │
 ┌───────────────────────────▼─────────────────────◄────┐
 │   AgendaEntry                                             │
 │                                                      │
 │   initialize  (expiriences, task, phone number)          
 
```python 

class Agenda():
    def add (self, agenda_entry)
    #agenda_ entry : instance of agenda entry
    #adds to a list of agenda entries
    pass

    def select_all (self):
        #return a list of entries instances
    pass


class AgendaEntry():

    def __init__(self, title, contents):
        #title string reprsentin the title 
        #content string representing the content
        pass

class TaskList():
    
    def add_task (self, task):
        #task_entry instance of task 
        pass


    def incomplete_task (self):
    # return a list of incomplete task
    pass

    def complete_task (self):
    #return list of complete task
    pass

class Task():

    def __init__(self, title):
    # title is a string to do 
    pass

    def mark_complete(self):
    #mark task as complete
    #return nothong
    pass


class ExtractPhone():
    
    def __init__(self, agenda)
    # agenda a instance of agenda
    pass

    def find_number (self)
    #return a list of numbers represneting a string
    pass

class ReadableEntry():

    def __init__(self, agenda)
    # agenda is a instance of agenda
    pass

    def extract (self, wpm, minute)
    #return the most readable entry 
    pass
 
3 - design test 

integration

    given an experience
    add expirience to a list

def test_add_experience_and_show_list():
    agenda = Agenda()
    entry_1 = AgendaEntry ("my title 1", "my contents 1")
    entry_2 = AgendaEntry ("my title 2", "my contents 2")
    agenda.add (entry_1)
    agenda.add (entry_2)
    assert agenda.select_all == [entry_1, entry_2]
    
 given tasks to do
 add the tasks and show ins the imcomplete list

def test_add_todo_and_show_incomplete():
    task_list = TaskList()
    todo_1 = Task ("my task 1")
    todo_2 = Task ("my task 2)
    task_list.add_task (todo_1)
    task_list.add_task (todo_2)
    todo_1.mark_complete()
    assert task_list.incomplete_task ==  [todo_2]

given a task to do
complete one task to do show complete 

def test_mark_complete_one_action():
    task_list = TaskList()
    todo_1 = Task (" my task 1")
    todo_2 = Task ("my task 2)
    task_list.add (todo_1)
    task_list.add (todo_2)  
    todo_1.mark_complete()
    assert task_list.complete() == [todo_1]
-
def test_find_number_in_agenda():
    agenda = Agenda()
    phone1 = AgendaEntry("numer 1", "0755644")
    phone2 = AgendaEntry ("number 2", "0733445)
    agenda.add(phone1)
    agenda.add(phone2)
    extract = ExtractPhone(agenda)
    find_number.extract() #=> ["0755644", "0733445]

    diary entry 
    with wpm 2 and minutes 2
    it gey agenda entry 

def test_readable_entry():
    agenda = Agenda()
    entry_1 = AgendaEntry ("title", "one two three four")
    agenda.add(entry_1)
    readable = ReadableEntry (agenda)
    readable.extract (wpm =2, minutes =2) # => entry_1


4 desing single test

# Agenda
# initialy there is not entries

agenda = Agenda()
agenda.select_all()# => [] 

#AgendaEntry 
entry = AgendaEntry("my title", "my contents")
entry.title # => "my title"
entry.contents # => "my contents"

#TaskList 
task_list = TaskList()
task_list.incomplete_task() #=> []

#Task
entry = Task ("my task 1")
entry.title #=> "my task 1" 





