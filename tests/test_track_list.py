from lib.track_list import *

# Give class the name of the song
def test_music():
    music = Music()
    addResult = music.add("Runaway - Kanye West")
    assert addResult == "Song has been added."

    assert music.list_tracks() == ["Runaway - Kanye West"]