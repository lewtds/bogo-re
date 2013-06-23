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
            {"result": "ư", "base": "u", "mod": "w"},
            {"result": "đ", "base": "d", "mod": "d"}
        ],
    "tone_addition": [],
    "undo": []
}

im["tone_addition"] = rules.gen_tone_addition_rules("fsrxj")

# A typical re_list (actually, a dict) looks like this:
# {
#     "character_creation": [
#         [r"^a([^a]*)a(.*)", "â"],
#         [r"^uo([^w]*)w(.*)", "ươ"]
#     ],
#     "tone_addition": [
#         [r'^ê([^r]*)r(.*)', 'ể'],
#     ]
# }
#
# For performance reasons, the regular expression string part is pre-compiled
# into an object beforehand.
re_list = rules.gen_re_list(im)


def process_word(word):
    def is_out_of_range(string, index):
        try:
            string[index]
            return False
        except:
            return True

    # Process the raw input string in phrases, each time iterating over the
    # whole string with a different set of rules.
    for rule_set in ["character_creation", "tone_addition"]:
        rule_set = re_list[rule_set]
        k = 0
        while not is_out_of_range(word, k):
            head, tail = word[:k], word[k:]
            for exp in rule_set:
                regexp_object, replace_with = exp[0], exp[1]
                new_string = regexp_object.sub(replace_with + r"\1\2", tail)
                if new_string != tail:
                    tail = new_string
                    # Decreasing k by one here is offset by k += 1 down below,
                    # effectively keeps the cursor from moving and reprocess
                    # the current character one more time. This is to allow
                    # undoing. ie: process_word("aaa") -> "âa" -> "a"
                    k -= 1
                    break

            word = head + tail
            k += 1

    return word
