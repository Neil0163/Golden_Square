def reading_time(text):
        if text == " ":
            raise Exception("No word read")
        else:
            words = text.split()
            word_count = len(words)
            return word_count / 200 