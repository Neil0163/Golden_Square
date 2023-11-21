# File: lib/diary.py

class Diary:
    def __init__(self):
        self.newList = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self.newList.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.newList

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        var = 0
        for i in self.newList:
            var += i.count_words()
        return var

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        var = 0
        for i in self.newList:
            var += i.reading_time(wpm)
        return var

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        empty_list = []
        words = minutes * wpm
        for i in self.newList:
            if i.count_words() < words:
                empty_list.append(i)
        num = float('inf')
        lowest_words = None
        for i in empty_list:
            if i.count_words() < num:
                lowest_words = i
        return lowest_words

