from typing import Optional, List, Tuple
from functools import reduce
from operator import itemgetter
from statistics import median

SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
SCORE_2 = { ")": 1, "]": 2, "}": 3, ">": 4}

PAIRS = {'{': '}', '[': ']', '<': '>', '(': ')'}

def check(line: str, close: List[str]) -> Tuple[Optional[str], List[str]]:
    print(line, close)
    fst = line[0]
    if len(line) == 1:
        if fst in PAIRS.keys():
            return None, close + [PAIRS[fst]]
        if len(close) > 0 and close[-1] == fst:
            return None, close[:-1]
        return fst, close

    if fst in PAIRS:
        return check(line[1:], close + [PAIRS[fst]])

    if len(close) > 0:
        if fst == close[-1]:
            return check(line[1:], close[:-1])
    return fst, close


# part 1
def test_harness():
    assert check(")", []) == (')', [])
    assert check("(", []) == (None, [')'])
    assert check("()", []) == (None, [])
    assert check("(())", []) == (None, [])
    assert check("()(", []) == (None, [')'])
    assert check("<()<>>", []) == (None, [])
    assert check("[(()[<>])]", []) == (None, [])
    assert check("[({(<(())[]>[[{[]{<()<>>", []) == (None, list("}}]])})]")[::-1])
    # assert check("[(()[<>])]({[<{<<[]>>(", []) == None
    # assert check("{([(<{}[<>[]}>{[]{[(<()>", []) == '}'
    # assert check("(((({<>}<{<{<>}{[]{[]{}", []) == None
    # assert check("[[<[([]))<([[{}[[()]]]", []) == ')'
    # assert check("[{[{({}]{}}([{[{{{}}([]", []) == ']'
    # assert check("{<[[]]>}<{[{[{[]{()[[[]", []) == None
    # assert check("[<(<(<(<{}))><([]([]()", []) == ')'
    # assert check("<{([([[(<>()){}]>(<<{{", []) == '>'
    # assert check("<{([{{}}[<[[[<>{}]]]>[]]", []) == None

if __name__ == "__main__":
    # part 1
    # print(sum([SCORE[b] for b, _ in (check(line, []) for line in open("input").read().strip().split("\n")) if b]))
    # part 2
    closers = [c for b, c in (check(line, []) for line in open("input").read().strip().split("\n")) if not b and c]
    scores = [reduce(lambda score, c: score*5 + SCORE_2[c], line[::-1], 0) for line in closers]
    print(median(scores))
    # part 2

