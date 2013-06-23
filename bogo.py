# -*- coding: utf-8 -*-

import rules


im = {
    "character_creation":
        [
            # Character creation rules
            {"result": "ươ", "base": "uo", "mod": "w"},
            {"result": "ă", "base": "a", "mod": "w"},
            {"result": "â", "base": "a", "mod": "a"},
            {"result": "ê", "base": "e", "mod": "e"},
            {"result": "ô", "base": "o", "mod": "o"},
            {"result": "ơ", "base": "o", "mod": "w"},
            {"result": "đ", "base": "d", "mod": "d"}
        ],
    "tone_addition": [],
    "undo": []
}

im["tone_addition"] = rules.gen_tone_addition_rules("fsrxj")
re_list = rules.gen_re_list(im)


def process_word(word):
    def is_out_of_range(string, index):
        try:
            string[index]
            return False
        except:
            return True

    # Process the raw input string in "phrases", each time iterating over the
    # whole string with a different set of rules.
    for rule_group in ["character_creation", "tone_addition"]:
        rule_group = re_list[rule_group]
        k = 0
        while not is_out_of_range(word, k):
            head, tail = word[:k], word[k:]
            for exp in rule_group:
                new_string = exp[0].sub(exp[1] + r"\1\2", tail)
                if new_string != tail:
                    tail = new_string
                    k -= 1
                    break

            word = head + tail
            k += 1

    return word



