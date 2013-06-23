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
