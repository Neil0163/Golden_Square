import pytest 
from lib.secret_diary import SecretDiary
from lib.S_Diary import SDiary

#When diary is locked you cant read it 

def test_locked_diary_cannot_be_read():
    diary = SDiary("My Contents")
    secret_dairy = SecretDiary(diary)
    with pytest.raises(Exception) as err:
        secret_dairy.read()
    assert str(err.value) == "Go away!"

#When we unlock the diary we can reead the dairy context


def test_unlocked_diary_can_be_read():
    diary = SDiary("My Contents")
    secret_dairy = SecretDiary(diary)
    secret_dairy.unlock()
    assert secret_dairy.read() == "My Contents" 
    

#When we lock the diary it can no longer be read

def test_relocked_diary_can_not_be_read():
    diary = SDiary("My Contents")
    secret_dairy = SecretDiary(diary)
    secret_dairy.unlock()
    secret_dairy.lock()
    with pytest.raises(Exception) as err:
        secret_dairy.read()
    assert str(err.value) == "Go away!"
    
