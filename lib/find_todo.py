def find_todo(text):
    if not text.strip():
        raise Exception("empty string")
    else:
        return "#TODO" in text.upper()