from lib.Mock_Track import Track

def test_matches_on_full_Title():
    track = Track("Forever", "Oasis")
    assert track.matches("Forever") == True 
    
def test_matches_on_partial_title():
    track = Track("Forever", "Oasis")
    assert track.matches("For") == True 
    
def test_matches_on_full_Artist():
    track = Track("Forever", "Oasis")
    assert track.matches("Oasis") == True 
    
def test_matches_on_partial_Artist():
    track = Track("Forever", "Oasis")
    assert track.matches("Oas") == True 
    
def test_matches_on_keyword_does_not_match():
    track = Track("Forever", "Oasis")
    assert track.matches("noMatch") == False
    
