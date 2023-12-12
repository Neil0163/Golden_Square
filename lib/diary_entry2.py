# File: lib/diary_entry.py
import math

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.title = title
        self.contents = contents
        self.current_state = 0

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        split_text = self.contents.split()
        return len(split_text)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        string = self.contents
        split_string = string.split()
        word_count = len(split_string)
        return math.trunc(word_count / wpm)

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        string = self.contents
        split_string = string.split()
        words = math.ceil(minutes * wpm)
        if len(split_string) < self.current_state + words:
            self.current_state = 0
        joined_text = " ".join(split_string[self.current_state:self.current_state + words])
        self.current_state += words
        return joined_text
