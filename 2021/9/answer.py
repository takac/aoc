from typing import List, Tuple
from operator import itemgetter
from collections import Counter, defaultdict
from math import prod

Point = Tuple[int, int]
Grid = List[List[int]]
def get_input() -> Grid:
    # return list(zip(*[[int(n) for n in line] for line in open('input').read().strip().split("\n")]))
    return list(zip(*[[int(n) for n in line] for line in open('test').read().strip().split("\n")]))

def get_adjanenct_pos(point: Point, max_x: int, max_y: int) -> List[Point]:
    x, y = point
    if x != 0:
        yield (x-1, y)
    if x != max_x - 1:
        yield (x+1, y)
    if y != 0:
        yield (x, y-1)
    if y != max_y - 1:
        yield (x, y+1)

def part_1(grid: Grid):
    max_x = len(grid)
    max_y = len(grid[0])
    print('max', max_x, max_y)
    low_points = []
    for i in range(max_x):
        for j in range(max_y):
            n = grid[i][j]
            adjancent = list(get_adjanenct_pos((i, j), max_x, max_y))
            nums = [grid[x][y] for (x, y) in adjancent if n >= grid[x][y]]
            adjancent = list(zip(adjancent, [grid[x][y] for (x, y) in adjancent]))
            if not nums:
                print((i, j), n, adjancent)
                low_points.append(n)
    print(sum(low_points) + len(low_points))


def basin_point(point: Point, max_x: int, max_y: int, grid: Grid) -> Tuple[Point, int]:
    x, y = point
    n = grid[x][y]

    lower = [((i, j), grid[i][j]) for (i,j) in get_adjanenct_pos((x,y), max_x, max_y) if grid[i][j] < n]
    if not lower:
        return ((x,y), n)

    basin_points = [basin_point((i,j), max_x, max_y, grid) for ((i, j), np) in lower]

    return sorted(basin_points, key=itemgetter(1))[0]

def part_2(grid: List[List[int]]) -> None:
    max_x = len(grid)
    max_y = len(grid[0])
    counter = defaultdict(int)
    for i in range(max_x):
        for j in range(max_y):
            n = grid[i][j]
            if n == 9:
                continue
            bp, np = basin_point((i, j), max_x, max_y, grid)
            counter[bp] = counter[bp] + 1
            print((i,j), n, bp, np)
    print(prod(map(itemgetter(1), sorted(counter.items(), key=itemgetter(1), reverse=True)[:3])))


if __name__ == "__main__":
    grid = get_input()
    for line in zip(*grid):
        print(line)
    # part_1(grid)
    part_2(grid)
