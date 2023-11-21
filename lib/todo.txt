# As a user
# So that I can keep track of my tasks
# I want to check if a text includes the string #TODO.

# Must include string as argument
# Must return something (a confirmation string?)

def check_todo(string):
    if type(string) is not str:
        raise Exception("You have not entered a string.")
    
    if "#TODO" in string:
        return "#TODO Is in this string."
    return "#TODO Is not in this string."