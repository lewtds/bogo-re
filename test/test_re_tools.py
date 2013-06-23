from nose.tools import eq_
from bogo import gen_re, gen_re_list


def test_gen_re():
    eq_(gen_re({"base": "a", "mod": "s"}), r"^a([^s]*)s(.*)")
    eq_(gen_re({"base": "uo", "mod": "w"}), r"^uo([^w]*)w(.*)")


def test_gen_re_list():
	im = [
	    {"result": "á", "base": "a", "mod": "s"},
	    {"result": "ươ", "base": "uo", "mod": "w"}
	]

	good_re_list = [
	    [r"^a([^s]*)s(.*)", "á"],
	    [r"^uo([^w]*)w(.*)", "ươ"]
	]

	re_list = gen_re_list(im)
	eq_(re_list, good_re_list)
