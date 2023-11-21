from lib.diary import *

def test_all_when_list_is_blank():
    call = Diary()
    assert call.all() == []

