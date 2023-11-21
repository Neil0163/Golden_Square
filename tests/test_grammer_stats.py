from lib.grammer_stats import *

def test_checker():
    grammar = GrammarStats()
    result = grammar.check("Ahsoufbsodbfoaubs.")
    result2 = grammar.check("asyfgasyibd")
    assert result == True
    assert result2 == False

def test_percentage_good():
    grammar = GrammarStats()
    grammar.check("Ahsoufbsodbfoaubs.")
    grammar.check("asyfgasyibd")
    grammar.check("And there she goes!")
    grammar.check("Hello world.")
    assert grammar.percentage_good() == 75