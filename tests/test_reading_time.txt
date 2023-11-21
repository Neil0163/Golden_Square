from lib.reading_time import *

words_100 = "In the realm of technology, innovation propels society forward. Constant advancements reshape how we connect, work, and live. From artificial intelligence transforming industries to breakthroughs in renewable energy addressing environmental concerns, the pace of change is relentless. This dynamic landscape demands adaptability and curiosity. In the digital age, information flows seamlessly, fostering a global exchange of ideas. However, challenges persist, requiring collective efforts for solutions. Education remains a cornerstone, empowering individuals to navigate this intricate landscape. As we navigate the future, the synergy of human ingenuity and technological progress will continue shaping a world that is both interconnected and ever-evolving"
words_200 = f"{words_100} {words_100}"
words_300 = f"{words_200} {words_100}"
words_400 = f"{words_200} {words_200}"
words_500 = f"{words_400} {words_100}"


# 100 words wil return a reading time of 0.5
def test_100_words():
    assert estimate_reading_times(words_100) == 0.5



# 200 words wil return a reading time of 1
def test_200_words():
    assert estimate_reading_times(words_200) == 1


# 300 words wil return a reading time of 1.5
def test_300_words():
    assert estimate_reading_times(words_300) == 1.5




# 400 words wil return a reading time of 2
def test_400_words():
    assert estimate_reading_times(words_400) == 2




# 500 words wil return a reading time of 2.5
def test_500_words():
    assert estimate_reading_times(words_500) == 2.5