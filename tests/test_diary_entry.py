from lib.diary_entry import DiaryEntry

"""
initialize with a title and contents
i can get that tittle and contents back  
"""

def test_constructs_gets_title_contents():
    diary_entry = DiaryEntry("My Title","My Contents")
    assert diary_entry.title == "My Title"
    assert diary_entry.contents == "My Contents"
    
"""
initialize with five words content
then count_words return five 
"""

def test_count_words_return_five():
    diary_entry = DiaryEntry ("My Title", " one two three four five")
    assert diary_entry.count_words() == 5 
    
    """
    with a five word content
    then reading time with wpm 2 return 3
    """
def test_reading_time ():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    assert diary_entry.reading_time(2) == 2.5
    
    """
    with a five word contents
    then reading chunk return the first chunk readable in time
    """
def test_readable_chunk_first_chunk():
    diary_entry = DiaryEntry("My title", "one two three four five")
    assert diary_entry.reading_chunk(2, 1) == "one two"
    
    """
    five words contents
    then second call reading chunk return the second chunk
    """
def test_readable_second_chunk():
    diary_entry = DiaryEntry("My title", "one two three four five")
    assert diary_entry.reading_chunk(2, 1) == "one two"
    assert diary_entry.reading_chunk(2, 1) == "three four"
    
    """
    five word content
    then third call remaining chunk returned
    """
def test_third_chunk():
    diary_entry = DiaryEntry("My title", "one two three four five")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1) 
    assert diary_entry.reading_chunk(2,1) == "five"
    
    """
    five words contents
    the fourht call start again from begining
    """
def test_fouth_chunk_star_again():
    diary_entry = DiaryEntry("My title", "one two three four five")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1) 
    diary_entry.reading_chunk(2,1)
    assert diary_entry.reading_chunk(2,1) == "one two"
    
    