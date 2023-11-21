from lib.diary_entry2 import *

def test_count_words_returns_int():
    call = DiaryEntry("Title 1", "Contents of Diary Entry")
    value = call.count_words()
    assert type(value) == int

def test_count_words_returns_correct_value():
    call = DiaryEntry("Title 1", "Contents of Diary Entry")
    assert call.count_words() == 4

def test_count_words_returns_0():
    call = DiaryEntry("", "")
    assert call.count_words() == 0

def test_reading_time_returns_numerical_value():
    call = DiaryEntry("Title 1", "Contents of Diary Entry")
    assert type(call.reading_time(1)) == int

def test_reading_time_returns_correct_value():
    call = DiaryEntry("Title 1", "Contents of Diary Entry")
    assert call.reading_time(1) == 4

def test_reading_chunk_returns_string():
    call = DiaryEntry("Title 1", "Contents of Diary Entry")
    assert type(call.reading_chunk(1, 2)) == str

def test_reading_chunk_returns_correct_value():
    call = DiaryEntry("Title 1", "Contents of Diary Entry")
    assert call.reading_chunk(2, 3) == "Contents of Diary Entry"

def test_reading_chunk_2nd_time():
    call = DiaryEntry("Title 1", "Contents of Diary Entry")
    call.reading_chunk(1, 2)
    assert call.reading_chunk(1, 2) == "Diary Entry"

def test_reading_chunk_3rd_time_starts_again():
    call = DiaryEntry("Title 1", "Contents of Diary Entry")
    call.reading_chunk(1, 2)
    call.reading_chunk(1, 2)
    assert call.reading_chunk(1, 2) == "Contents of"