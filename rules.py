import re
from common import *


def gen_tone_addition_rules(tone_mod_keys):
    rules = []

    # Single vowel rules
    tmp_rules = []  # These rules have to be the last in 'rules', whilst
                    # calculated before the following 2 groups of rules
    for base in "aăâeêioôơuưy":
        for index, tone_mod in enumerate(tone_mod_keys):
            tmp_rules.append({
                "result": tone_map[base][index],
                "base": base,
                "mod": tone_mod
            })

    # Complex open vowel rules
    for mod in tone_mod_keys:
        for vowel in OPEN_VOWELS:
            # Tone placement

            head, core, tail = vowel[:-2], vowel[-2], vowel[-1:]
            core = query(tmp_rules, {"base": core, "mod": mod})[0]["result"]
            rules.append({
                "result": head + core + tail,
                "base": vowel,
                "mod": mod,
                "open": True})

    # Complex closed vowel rules
    for mod in tone_mod_keys:
        for vowel in CLOSED_VOWELS:
            head, core = vowel[:-1], vowel[-1]
            core = query(tmp_rules, {"base": core, "mod": mod})[0]["result"]
            rules.append({
                "result": head + core,
                "base": vowel,
                "mod": mod,
                "open": False})

    rules += tmp_rules

    return rules


def gen_re_list(im):
    re_list = {}
    for group in im.keys():
        tmp_list = []
        for rule in im[group]:
            tmp_list.append([gen_re(rule), rule["result"]])
        re_list[group] = tmp_list
    return re_list


def gen_re(im_rule):
    # TODO Some explanation here
    if "open" in im_rule:
        if im_rule["open"] == False:
            reg = r"" + \
                "^{0}([^{1}]*){1}([{2}]*)$" \
                .format(im_rule["base"], im_rule["mod"], CONSONANTS)
        else:
            reg = r"" + \
                "^{0}([^{1}{2}]*){1}()$" \
                .format(im_rule["base"], im_rule["mod"], CONSONANTS)
    else:
        reg = r"" + \
            "^{0}([^{1}]*){1}(.*)".format(im_rule["base"], im_rule["mod"])
    return re.compile(reg)
