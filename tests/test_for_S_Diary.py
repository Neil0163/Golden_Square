from unittest.mock import Mock 
from lib.S_Diary import SDiary
import pytest 

# when diary is intially is locked so you cant read it 
def test_can_read_contents():
    diary = SDiary("My contents")
    assert diary.read() == "My contents"
    