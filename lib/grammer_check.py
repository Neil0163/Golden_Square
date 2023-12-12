# As a user
# So that I can improve my grammar
# I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

# Check that the text starts with capital letter and ends with either a !, ., or ?
# Make sure argument is string
# Check that first item of string is upper case
# Check that last element of string is either !, ., or ?
# If both return true then return confirmation string
# If either or all return false then return fail string

def verify_grammar(string):
    if type(string) is not str:
        raise Exception("This is not a string.")
    punctuation = "!.?"
    if string[0].isupper() and string[-1] in punctuation:
        return "Correct grammar."
    return "Incorrect grammar."
