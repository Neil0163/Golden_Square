from unittest.mock import Mock 
from lib.secret_diary import SecretDiary
import pytest 

# when diary is intially is locked so you cant read it 


def test_locked_diary_cannot_be_read():
    diary = Mock()
    secret_dairy = SecretDiary(diary)
    with pytest.raises(Exception) as err:
        secret_dairy.read()
    assert str(err.value) == "Go away!"
    diary.read.assert_not_called()
    
#when unlocked you ca read the diary 
def test_when_unlocked_you_can_read_the_diary():
    diary = Mock()
    diary.read.return_value = "Cool Contents"
    secret_dairy = (diary)
    secret_dairy.unlock()
    assert secret_dairy.read() == "Cool Contents"
    diary.read.assert_called()
    
def test_relocked_diary_can_not_be_read():
    diary = Mock()
    secret_dairy = SecretDiary(diary)
    secret_dairy.unlock()
    secret_dairy.lock()
    with pytest.raises(Exception) as err:
        secret_dairy.read()
    assert str(err.value) == "Go away!"
    diary.read.assert_not_called()