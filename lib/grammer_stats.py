class GrammarStats:
    def __init__(self):
        self.results = []
  
    def check(self, string):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if type(string) is not str:
            raise Exception("This is not a string.")
        punctuation = "!.?"
        if string[0].isupper() and string[-1] in punctuation:
            self.results.append(True)
            return True
        self.results.append(False)
        return False
  
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        length = len(self.results)
        good_length = 0
        for item in self.results:
            if item == True:
                good_length+=1
        percentage = good_length/length * 100
        return percentage
