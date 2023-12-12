def make_snippet(string):
    if type(string) is not str:
        raise Exception("This is not a string.")
    empty = string.split(" ")
    print(empty)
    if len(empty) > 5:
        new_string = " ".join(empty[0:5])
        return f"{new_string}..."
    
    return f"{string}"
