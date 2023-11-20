
class Diary:
    def __init__(self):
        self._entries = []

    def add(self, entry):
        self._entries.append (entry)

    def all(self):
        return self._entries

    def count_words(self):
        total = 0 
        for entry in self._entries:
                total += entry.count_words()
        return total

    def reading_time(self, wpm):
        if self._entries == []:
            raise Exception ("No entries added yet")
        word_count = self.count_words()
        return word_count / wpm
    
    def find_best_entry_for_reading_time(self, wpm, minutes): 
        if self._entries == []:
            raise Exception ("No entries added yet")   
        words_read = wpm * minutes
        most_redable_entries = None
        longest_found = 0
        for entry in self._entries:
            if entry.count_words() <= words_read:
                if entry.count_words() > longest_found:
                    most_redable_entries = entry
                    longest_found = entry.count_words()
        return most_redable_entries


