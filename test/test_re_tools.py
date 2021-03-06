from nose.tools import eq_
from rules import gen_re, gen_re_list
import re


def test_gen_re():
    eq_(gen_re({"base": "a", "mod": "s"}), {"base": "a", "mod": "s", "regexp": re.compile(r"^a([^s]*)s(.*)")})
    eq_(gen_re({"base": "uo", "mod": "w"}), {"base": "uo", "mod": "w", "regexp": re.compile(r"^uo([^w]*)w(.*)")})


def test_gen_re_list():
    im = {
        "tone_addition": [
        {"result": "á", "base": "a", "mod": "s"},
        {"result": "ươ", "base": "uo", "mod": "w"}
    ]}

    good_re_list = {
        "tone_addition": [
        {"result": "á", "base": "a", "mod": "s", "regexp": re.compile(r"^a([^s]*)s(.*)")},
        {"result": "ươ", "base": "uo", "mod": "w", "regexp": re.compile(r"^uo([^w]*)w(.*)")}
    ]}


    re_list = gen_re_list(im)
    eq_(re_list, good_re_list)
