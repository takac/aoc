from typing import Tuple, Literal, List, Iterable, Callable, NewType
from operator import mul
from functools import reduce

def raw_directions() -> Iterable[Tuple[Literal['forward', 'down', 'up'], int]]:
    for line in open("input").read().strip().split("\n"):
        direction, n = line.split(" ", 1)
        if direction not in ('forward', 'down', 'up'):
            raise Exception("Bad direction: {direction}")
        yield direction, int(n)


# part 1
def get_directions() -> Iterable[Tuple[int, int]]:
    for direction, n in raw_directions():
        if direction == 'forward':
            yield (n, 0)
        elif direction == 'down':
            yield (0, n)
        else:
            yield (0, -n)


# part 2
def get_directions_2() -> Iterable[Callable[[int, int, int], Tuple[int, int, int]]]:
    for direction, n in raw_directions():
        def f(x: int, y: int, a: int) -> Tuple[int, int, int]:
            if direction == 'forward':
                return x + n, y + (a * n), a
            elif direction == 'down':
                return x, y, a + n
            else:
                return x, y, a - n
        yield f

if __name__ == "__main__":
    print("Part1:", mul(*list(map(sum, zip(*get_directions())))))
    x, y, a = reduce(lambda vals, f: f(*vals), get_directions_2(), (0, 0, 0))
    print("Part2:", (x * y))
