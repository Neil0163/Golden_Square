from lib.diary import *
from lib.diary_entry2 import *

def test_all_returns_two():
    Entry1 = DiaryEntry("Title 1", "Contents 1")
    Entry2 = DiaryEntry("Title 2", "Contents 2")
    diaryVar = Diary()
    diaryVar.add(Entry1)
    diaryVar.add(Entry2)
    assert diaryVar.all() == [Entry1, Entry2]

def test_count_words_returns_int():
    Entry1 = DiaryEntry("Title 1", "Contents 1")
    Entry2 = DiaryEntry("Title 2", "Contents 2")
    diaryVar = Diary()
    diaryVar.add(Entry1)
    diaryVar.add(Entry2)
    assert type(diaryVar.count_words()) == int

def test_count_words_returns_correct():
    Entry1 = DiaryEntry("Title 1", "Contents 1")
    Entry2 = DiaryEntry("Title 2", "Contents 2")
    diaryVar = Diary()
    diaryVar.add(Entry1)
    diaryVar.add(Entry2)
    assert diaryVar.count_words() == 4

def test_count_words_returns_0():
    Entry1 = DiaryEntry("", "")
    diaryVar = Diary()
    diaryVar.add(Entry1)
    assert diaryVar.count_words() == 0

def test_reading_time_returns_int():
    Entry1 = DiaryEntry("Title 1", "Contents 1")
    diaryVar = Diary()
    diaryVar.add(Entry1)
    assert type(diaryVar.reading_time(1)) == int

def test_reading_time_returns_correct_value():
    Entry1 = DiaryEntry("Title 1", "Contents 1")
    Entry2 = DiaryEntry("Title 2", "Contents 2")
    diaryVar = Diary()
    diaryVar.add(Entry1)
    diaryVar.add(Entry2)
    assert diaryVar.reading_time(2) == 2

def test_best_entry_returns_instance_of_DiaryEntry():
    Entry1 = DiaryEntry("Title 1", "Contents 1 Contains a bunch of waffle")
    Entry2 = DiaryEntry("Title 2", "Contents 2")
    diaryVar = Diary()
    diaryVar.add(Entry1)
    diaryVar.add(Entry2)
    assert diaryVar.find_best_entry_for_reading_time(1, 3) == Entry2