from typing import Tuple, List

Point = Tuple[int, int]
Map = List[List[int]]

def load_points() -> List[Tuple[Point, Point]]:
    return [tuple(tuple(int(p) for p in points.split(",")) for points in line.split(' -> ')) for line in open("input").read().strip().split('\n')]

def create_map(n):
    return [[0 for i in range(n)] for j in range(n)]

def draw_map(map: List[List[int]]):
    return "\n".join("".join("." if p == 0 else str(p) for p in line) for line in zip(*map))

def update_map(p1: Point, p2: Point, map: Map):
    print("check for", p1, p2)
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for i in range(y1, y2+1):
            print("updatey", x1, i)
            map[x1][i] = map[x1][i] + 1
    elif y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for i in range(x1, x2+1):
            print("updatex", i, y1)
            map[i][y1] = map[i][y1] + 1
    # part 2
    else:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        y_diff = 1
        if y1 > y2:
            y_diff = -1
        x3, y3 = x1, y1
        while True:
            print("updatez", x3, y3)
            map[x3][y3] = map[x3][y3] + 1
            x3 = x3 + 1
            y3 = y3 + y_diff
            if (x3 > x2):
                break

def count_gt_0(map: Map):
    return sum(0 if p < 2 else 1 for line in map for p in line)


if __name__ == "__main__":
    print(load_points())
    map = create_map(1000)

    for p1, p2 in load_points():
        # print(draw_map(map))
        update_map(p1, p2, map)
    # end = draw_map(map)
    print(count_gt_0(map))

