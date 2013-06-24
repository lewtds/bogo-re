import re
from common import *

tone_affinities = {
    "a": "àáảãạ",
    "ă": "ằắẳẵặ",
    "â": "ầấẩẫậ",
    "e": "èéẻẽẹ",
    "ê": "ềếểễệ",
    "i": "ìíỉĩị",
    "o": "òóỏõọ",
    "ô": "ồốổỗộ",
    "ơ": "ờớởỡợ",
    "u": "ùúủũụ",
    "ư": "ừứửữự",
    "y": "ỳýỷỹỵ"
}


def gen_tone_addition_rules(tone_mod_keys):
    rules = []

    # Single vowel rules
    tmp_rules = []  # These rules have to be the last in 'rules', whilst
                    # calculated before the following 2 groups of rules
    for base in tone_affinities.keys():
        for index, tone_mod in enumerate(tone_mod_keys):
            tmp_rules.append({
                "result": tone_affinities[base][index],
                "base": base,
                "mod": tone_mod
            })

    for index, mod in enumerate(tone_mod_keys):
        # open compound vowel rules
        # eg: iếu, oéo, áo -> tone mark at the second position from the right
        for vowel in OPEN_VOWELS:
            # Some observation here: processing compound vowels is no different
            # to processing a single vowel isolated from its surrounding. So we
            # use `query` to lookup that single vowel's rule and copy it here.
            head, core, tail = vowel[:-2], vowel[-2], vowel[-1:]
            core = tone_affinities[core][index]
            rules.append({
                "result": head + core + tail,
                "base": vowel,
                "mod": mod,
                "open": True})

        # closed compound vowel rules
        # eg: án, iến -> tone mark at the first position from the right
        for vowel in CLOSED_VOWELS:
            head, core = vowel[:-1], vowel[-1]
            core = tone_affinities[core][index]
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
            tmp_list.append(gen_re(rule))
        re_list[group] = tmp_list
    return re_list


def gen_re(im_rule):
    # TODO Some explanation here
    if "open" in im_rule:
        if im_rule["open"] == False:
            reg = r"" + \
                "^{0}([^{1}]*){1}(.*)$" \
                .format(im_rule["base"], im_rule["mod"])
        else:
            reg = r"" + \
                "^{0}([^{1}{2}]*){1}()$" \
                .format(im_rule["base"], im_rule["mod"], CONSONANTS)
    else:
        reg = r"" + \
            "^{0}([^{1}]*){1}(.*)".format(im_rule["base"], im_rule["mod"])
    im_rule["regexp"] = re.compile(reg)
    return im_rule
