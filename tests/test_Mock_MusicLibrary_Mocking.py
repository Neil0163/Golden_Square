from unittest.mock import Mock
from lib.Mock_MusicLibary import MusicLibrary

def test_for_serches_keyword():
    library = MusicLibrary()
    fake_matching = fakematching()
    library.add(fake_matching)
    fake_not_matching = notfakematching
    library.add(fake_not_matching())
    assert library.search("hi") == [fake_matching]
    
class fakematching():
    def matches(self, keyword):
        return True

class notfakematching():
    def matches(self, keyword):
        return False
    
#**************************************************************#

def test_for_searches_keyword2():
    library = MusicLibrary()
    fake_matching2 = Mock()
    fake_matching2.matches.return_value = True
    library.add(fake_matching2)
    fake_not_matching = Mock()
    fake_not_matching.matches.return_value = False
    library.add(fake_not_matching)
    assert library.search("hi") == [fake_matching2]
    