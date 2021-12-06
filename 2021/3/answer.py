from typing import List
from collections import Counter

def get_bit_words() -> List[str]:
    return open("input").read().strip().split("\n")

# --- part 1 ---
def most_common_bits(words: List[str]) -> str:
    return "".join(Counter(col).most_common()[0][0] for col in zip(*words))

def invert_word(word: str):
    return "".join(("0","1")[int(i != "1")] for i in word)
# -- end of part 1

# --- part 2 ---
def most_common_bit(words: List[str], col: int, default: str, order: int = 1) -> str:
    most_common = Counter(list(zip(*words))[col]).most_common()[::order]
    top, snd = most_common[0], most_common[1]
    if top[1] == snd[1]:
        return default
    return top[0]

def oxygen_generator_rating(words: List[str]) -> str:
    for col in range(len(words[0])):
        top = most_common_bit(words, col, '1')
        words = [word for word in words if word[col] == top]
        if len(words) == 1:
            return words[0]


def co2_scrubber_rating(words: List[str]) -> str:
    for col in range(len(words[0])):
        top = most_common_bit(words, col, '0', order=-1)
        words = [word for word in words if word[col] == top]
        if len(words) == 1:
            return words[0]


if __name__ == "__main__":
    print(len(get_bit_words()))
    # --- part 1 ---
    # word = most_common_bits(get_bit_words())
    # print("most_common", word, int(word, 2))
    # inverted_word = invert_word(word)
    # print("invert", inverted_word, int(inverted_word, 2))
    # print(int(word, 2) * int(inverted_word, 2))
    # --- part 2 ---
    o2_rating = oxygen_generator_rating(get_bit_words())
    co2_rating = co2_scrubber_rating(get_bit_words())
    print('o2', o2_rating)
    print('co2', co2_rating)
    print(int(o2_rating, 2) * int(co2_rating, 2))
