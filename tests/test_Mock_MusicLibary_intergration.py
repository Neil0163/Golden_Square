from lib.Mock_MusicLibary import MusicLibrary
from lib.Mock_Track import Track
import pytest

def test_for_adding_a_song_and_listing():
    library = MusicLibrary()
    track_1 = Track("My Track", "my Artitst")
    track_2 = Track("My Track", "My Artist")
    library.add(track_1)
    library.add(track_2)
    assert library.tracks == [track_1, track_2]
    
#@pytest.mark.skip   
def test_for_full_track_name():
    library = MusicLibrary()
    track_1 = Track("Forever", "Oasis")
    track_2 = Track("Sky full of stars", "Coldplay")
    library.add(track_1)
    library.add(track_2)
    assert library.search("Forever") == [track_1]
    
def test_empty_list_initally():
    library = MusicLibrary()
    assert library.tracks == []
    

    