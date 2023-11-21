# A function called count_words that takes a string 
# as an argument and returns the number of words in that string.

def count_word(string):
    if type(string) is not str:
        raise Exception("NOT A STRING!!!")
    split_string = string.split(" ")
    count = len(split_string)
    return count