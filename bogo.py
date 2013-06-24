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

# A typical im after gen_re_list() looks just like the original one, but with
# each of its rules getting a new "regexp" key:
#
# {
#     "character_creation": [...],
#     "tone_addition": [
#         {"result": "á", "base": "a", "mod": "s", "regexp": re.compile(r"^a([^s]*)s(.*)")},
#         {"result": "ươ", "base": "uo", "mod": "w", "regexp": re.compile(r"^uo([^w]*)w(.*)")}
#     ],
#     ...
# }
#
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
            for rule in rule_set:
                # This line makes it FASSSTEEERRRR!!!
                if word.find(rule["base"]) != -1:
                    new_string = rule["regexp"].sub(rule["result"] + r"\1\2", tail)
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

print(process_word("chuyênr"))
