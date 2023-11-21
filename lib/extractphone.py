import re
class ExtractPhone():
    
    def __init__(self, agenda):
        self.agenda = agenda

    def find_number (self):
        phonenumbers = []
        for entry in self.agenda:
            contents = entry.contents
            phonenumbers =+ re.findall (r"0,[0 -9]{10}", contents)
            return phonenumbers