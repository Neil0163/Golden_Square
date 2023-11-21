from lib.user_stories import *

def test_tracker():
    tracker = Tracker()
    tracker.add("#TODO Clock out")
    result = tracker.list_items()
    assert result == ["#TODO Clock out"]
    tracker.complete_task("#TODO Clock out")
    result = tracker.list_items()
    assert result == []