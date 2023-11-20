import pytest
from lib.diary import Diary

"""
empty list of entries 
"""
def test_empty_list_of_entries():
    diary = Diary()
    assert diary.all() == []
    
"""
reading_time should raise an error
"""
def test_reading_time_raises_error():
    diary = Diary()
    with pytest.raises (Exception) as err:
        diary.reading_time(2)
    assert str (err.value) == "No entries added yet"
    
    """
    intitially find beest entry for reading shoul raise error
    """
def test_initially_find_best_raise_error():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.find_best_entry_for_reading_time(2,2)
    assert str(err.value) == "No entries added yet"
    