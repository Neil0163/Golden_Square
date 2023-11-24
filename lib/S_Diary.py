# File: lib/diary.py

class SDiary:
    def __init__(self, contents):
        # contents is a string
        self._contents = contents

    def read(self):
        return self._contents