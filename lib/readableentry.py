class ReadableEntry():

    def __init__(self, agenda):
        self.agenda = agenda

    def extract (self, wpm, minutes):
        entries = self.agenda.all()
        if self.readable_in_time(wpm, minutes, entries[0]):
            return entries[0]
        else:
            return None
        
    def readable_in_time (self, wpm, minutes, entry):
        leng_readable = wpm * minutes
        return self.word_count(entry.contents) <= leng_readable 
            
        
    def word_count(self, string):
        return len(string.split(" "))