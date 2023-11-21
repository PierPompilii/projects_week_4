class Agenda():
    def __init__(self):
        self.agenda_list = []
        
    def add (self, agenda_entry):
        self.agenda_list.append (agenda_entry)

    def select_all (self):
        return self.agenda_list
