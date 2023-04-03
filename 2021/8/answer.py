from typing import List, Tuple, Set
from functools import reduce
from collections import defaultdict

def get_input() -> Tuple[List[List[str]], List[List[str]]]:
    return [tuple([seg.split() for seg in line.split(" | ", 1)])
            for line in open("input").read().strip().split("\n")]


def get_input_2() -> Tuple[List[List[Set[str]]], List[List[Set[str]]]]:
    return [
        tuple(
            [set(s) for s in seg.split()]
            for seg in line.split(" | ", 1)
        )
        for line in open("input").read().strip().split("\n")
    ]

def get_mapping(input: List[Set[str]]) -> List[Set[str]]:
    # c is a lookup by number of segments
    c = defaultdict(list)
    for i in input:
        c[len(i)].append(i)

    right = c[2][0]
    # 7 digit - 1 digit
    top = (c[3][0] - right)
    # all len 5s digits: 2, 3, 5 only share top+middle+bottom
    bottom = (c[5][0] & c[5][1] & c[5][2]) - top - c[4][0]
    middle = (c[5][0] & c[5][1] & c[5][2]) - top - bottom
    left_high = (c[4][0] - right) - middle
    left_low = c[7][0] - top -  bottom - c[4][0]
    # intersection 6, 0, 9
    right_low = ((c[6][0] & c[6][1]) & c[6][2]) - top - left_high - bottom
    right_high = c[7][0] - top - middle - bottom - right_low - left_high - left_low

    return [
       right_high | right_low | top | bottom | left_high | left_low,
       right,
       top | middle | bottom | right_high | left_low,
       top | middle | bottom | right,
       middle | right | left_high,
       top | bottom | middle | right_low | left_high,
       top | bottom | middle | right_low | left_low | left_high,
       top | right_high | right_low,
       right_high | right_low | top | middle | bottom | left_high | left_low,
       right_high | right_low | top | middle | bottom | left_high ,
   ]



if __name__ == "__main__":
    # part 1
    # lines = get_input()
    # counter = 0
    # for input, output in lines:
    #     for chunk in output:
    #         if len(chunk) in (2, 3, 4, 7):
    #             counter = counter + 1
    # print(counter)
    # part 2
    lines = get_input_2()
    out = []
    for input, output in lines:
        mapping = get_mapping(input)
        n = int("".join(str([idx for idx, m in enumerate(mapping) if set(o) == m][0]) for o in output))
        out.append(n)
    # test_results = [8394, 9781, 1197, 9361, 4873, 8418, 4548, 1625, 8717, 4315]
    # assert test_results == out
    print(sum(out))

