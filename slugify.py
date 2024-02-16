from constants import AZ_TO_EN_LETTERS, SYMBOLS


__all__ = (
    "map_func",
    "replace_symbols"
)

def map_func(char: str):
    is_symbol = char in SYMBOLS
    return " " if is_symbol else char

def replace_symbols(s: str):
    char_list = map(map_func, s)
    return "".join(char_list)

def get_announcement_name():
    n = input()
    return n

def simplify_name(s: str):
    return s.strip().lower()

def split_words(s: str):
    return s.split()

def construct_name_with_dashes(words: list) -> str:
    return "-".join(words)

def convert_az_to_en_letters(_name: str):
    final_name = ""
    for char in _name:
        if char in AZ_TO_EN_LETTERS.keys(): # ç
            final_name += AZ_TO_EN_LETTERS[char] # ç -> c
            continue
        final_name += char # r
    return final_name
# "iphone@@@@14"
# import string
# string.printable
def generate_slug() -> str:
    name = get_announcement_name()
    new_name = simplify_name(name)
    word_list = split_words(new_name)
    constructed_name = construct_name_with_dashes(word_list)
    result = convert_az_to_en_letters(constructed_name)
    return result


if __name__ == "__main__":
    # slug = generate_slug()
    # print(slug)
    from string import punctuation
    print(punctuation)