# As a user
# So that I can keep track of my music listening
# I want to add tracks I've listened to and see a list of them.

class Music:
    def __init__(self):
        self.songs = []

    def add(self, string):
        self.songs.append(string)
        return "Song has been added."

    def list_tracks(self):
        return self.songs