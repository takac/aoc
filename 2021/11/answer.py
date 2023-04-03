from typing import List, Tuple

Point = Tuple[int, int]
Grid = List[List[int]]

def get_adjanenct_pos(point: Point, max_x: int, max_y: int) -> List[Point]:
    x, y = point
    if x != 0:
        yield (x-1, y)
        if y != 0:
            yield (x-1, y-1)
        if y < (max_y - 1):
            yield (x-1, y+1)
    if x < (max_x - 1):
        yield (x+1, y)
        if y != 0:
            yield (x+1, y-1)
        if y < (max_y - 1):
            yield (x+1, y+1)
    if y != 0:
        yield (x, y-1)
    if y < max_y - 1:
        yield (x, y+1)

def get_grid() -> Grid:
    # return list(zip(*[[int(n) for n in line] for line in open('input').read().strip().split("\n")]))
    return list(zip(*[[int(n) for n in line] for line in open('test').read().strip().split("\n")]))

def flash_

if __name__ == "__main__":
    grid = get_grid()
    flashed = [[False for i in range(10)] for j in range(10)]
    # print(list(get_adjanenct_pos((9,9), 10, 10)))
    # print(list(get_adjanenct_pos((0,0), 10, 9)))
    # print(list(get_adjanenct_pos((1,1), 10, 10)))
    # print(list(get_adjanenct_pos((8,8), 10, 10)))
    for tick in range(10):
        print("tick")
        for line in zip(*grid):
            print(line)
        for i in range(10):
            for j in range(10):
                grid[i][j] = grid[i][j] + 1
                if grid[i][j] > 9:
                    for (x,y) in get_adjanenct_pos((i, j), 10, 10):
                        grid

