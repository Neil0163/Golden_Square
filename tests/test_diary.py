from lib.diary_entry import *

def test_format():
    diary = DiaryEntry("Seans Book", "Chapter 1: Waffle")
    assert diary.format() == "Seans Book: Chapter 1: Waffle"

def test_count_words():
    diary = DiaryEntry("Seans Book", "Chapter 1: Waffle")
    count_words = diary.count_words()
    assert count_words == 4

def test_reading_time():
    diary = DiaryEntry("Seans Book", "Chapter 1: Waffle")
    reading_time = diary.reading_time(200)
    assert reading_time == 0.02

def test_reading_chunk():
    diary = DiaryEntry("Seans Book", "Chapter 1: Waffle")
    reading_chunk = diary.reading_chunk(2, 1)
    assert reading_chunk == "Seans Book"