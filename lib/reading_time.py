# As a user
# So that I can manage my time
# I want to see an estimate of reading time for a
# text, assuming that I can read 200 words a minute.

# function that takes a string as an arguement
# needs to count the number of words
# split the string
# length of list to count words
# need to mulitply word count by 0.5

def estimate_reading_times(string):
    split_string = string.split()
    word_count = len(split_string)
    return word_count * 0.005
