from lib.diary import Diary
from lib.diary_entry import DiaryEntry

"""
add two diary entries
see list back  
"""
def test_adds_and_lists_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "My content 1")
    entry_2 = DiaryEntry ("Title 2", "My content 2")
    diary.add(entry_1)
    diary.add (entry_2)
    assert diary.all() == [entry_1, entry_2]
    
    """
    add two entries
    call #count_words
    get the sum of all words in the contents
    """
def test_count_words_returns_all_words():
    diary = Diary()
    entry_1 = DiaryEntry ("Title 1", "one two")
    entry_2 = DiaryEntry ("Tittle 2", "three four five")
    diary.add(entry_1)
    diary.add (entry_2)
    assert diary.count_words() == 5 
    
    """
    add two diary entries with total lenght of 5
    and i can #reading_time with a wpm of 2
    then total reading time is 3
    """
def test_reading_time_return_time_to_read():
    diary = Diary()
    entry_1 = DiaryEntry ("Title 1", "one two")
    entry_2 = DiaryEntry ("Tittle 2", "three four five")
    diary.add(entry_1)
    diary.add (entry_2)
    assert diary.reading_time(2) == 2.5
    
    """
    given i add two diary entries, one long and one short
    and call #find_best_entry_for_reading_time
    with wpm and minutes that means i can only read short one
    then #find_best_entry_for_reading_time return the short one
    
    """
def test_find_best_entry_for_entry():
    diary = Diary()
    entry_1 = DiaryEntry ("Title 1", "one two three")
    entry_2 = DiaryEntry ("Tittle 2", " one two three four five six seven")
    diary.add(entry_1)
    diary.add (entry_2)  
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_1
    
    """
    given add entry
    and i canll #find_best_entry_for_reading
    with wpm and minutes that means i cannot read 
    then rerturn none
    """
def test_find_best_entry_for_reading_return_none():
    diary = Diary()
    entry_1 = DiaryEntry("My title 1", "one two three four five six seven eight nine")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 3) == None 
    
    """
    given i add two entries
    and call find best time for reading time 
    with wpm and minutes that means i could read both
    return the longer one
    """
    
def test_find_best_entry_return_long():
    diary = Diary()
    entry_1 = DiaryEntry ("Title 1", "one two three")
    entry_2 = DiaryEntry ("Tittle 2", " one two three four five six seven")
    diary.add(entry_1)
    diary.add (entry_2)  
    assert diary.find_best_entry_for_reading_time(2, 4) == entry_2 
     