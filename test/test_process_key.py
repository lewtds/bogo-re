from nose.tools import eq_
from bogo import process_word


def test_single_vowel_words():
    eq_(process_word("cans"), "cán")
    eq_(process_word("cêns"), "cến")
    eq_(process_word("cuns"), "cún")
    eq_(process_word("cins"), "cín")
    eq_(process_word("xaay"), "xây")
    eq_(process_word("ddoiwf"), "đời")
    eq_(process_word("mowis"), "mới")
    eq_(process_word("nguwngf"), "ngừng")
    eq_(process_word("ddonogj"), "động")


def test_complex_closed_vowels():
    eq_(process_word("thuownrg"), "thưởng")
    eq_(process_word("chuyener"), "chuyển")


def test_failed_tests():
    test_cases = [
        ('biesue', 'biếu'),
        ('bieseu', 'biếu'),
        ('bieesu', 'biếu'),
        ('biereu', 'biểu'),
        ('bieeru', 'biểu'),
        ('bierue', 'biểu'),
        ('booong', 'boong'),
        ('booosng', 'boóng'),
        ('booonsg', 'boóng'),
        ('booongs', 'boóng'),
        ('buofoi', 'buồi'),
        ('buofio', 'buồi'),
        ('buoofi', 'buồi'),
        ('buoori', 'buổi'),
        ('buorio', 'buổi'),
        ('buoroi', 'buổi'),
        ('buosuw', 'bướu'),
        ('buwosuw', 'bướu'),
        ('buowsu', 'bướu'),
        ('buwowsu', 'bướu'),
        ('buwoswu', 'bướu'),
        ('buoswu', 'bướu'),
        ('buwowri', 'bưởi'),
        ('buowri', 'bưởi'),
        ('buworiw', 'bưởi'),
        ('buworwi', 'bưởi'),
        ('buorwi', 'bưởi'),
        ('buoriw', 'bưởi')]

    def atomic(input_, expected):
        eq_(process_word(input_), expected)

    for case in test_cases:
        yield atomic, case[0], case[1]
