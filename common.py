tone_map = {
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


VOWELS = "àáảãạaằắẳẵặăầấẩẫậâèéẻẽẹeềếểễệêìíỉĩịi" \
    "òóỏõọoồốổỗộôờớởỡợơùúủũụuừứửữựưỳýỷỹỵy"

# Open vowels are vowels that can end a word (they are open-ended)
# while closed vowels are those that have to be followed by some
# consonants.

# Keep these lists sorted by length
OPEN_VOWELS = (
    'ươu',
    'ươi',
    'ưu',
    'ưi',
    'ưa',
    'ơi',
    'ôi',
    'êu',
    'ây',
    'âu',
    'yêu',
    'uơ',
    'uôi',
    'uê',
    'uây',
    'uyu',
    'uya',
    'uy',
    'ui',
    'ua',
    'oi',
    'oeo',
    'oe',
    'oay',
    'oao',
    'oai',
    'oa',
    'iêu',
    'iu',
    'ia',
    'eo',
    'ay',
    'au',
    'ao',
    'ai'
)

CLOSED_VOWELS = (
    'ươ',
    'yê',
    'uô',
    'uê',
    'uâ',
    'uyê',
    'uy',
    'oă',
    'oo',
    'oe',
    'oa',
    'iê',
)

CONSONANTS = "bcdghklmnprstvxđ"


def query(object_list, constrains):
    """
    Query a list of objects for the objects that have their keys matching
    what's required in constrains, which is a dictionary. Similar to SQL's
    SELECT statement.
    """
    objs = []
    for obj in object_list:
        match = True
        try:
            for key in constrains.keys():
                if obj[key] != constrains[key]:
                    match = False
                    break
            if match == True:
                objs.append(obj)
        except IndexError:
            pass
    return objs
