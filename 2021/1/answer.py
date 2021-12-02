depths = [int(i) for i in open("input").read().strip().split("\n")]

def part_1():
    # for d1, d2 in zip(depths, depths[1:]):
    #     print(d1, d2, "Increased" if d2 > d1 else "Decreased")
    return len([d1 for d1, d2 in zip(depths, depths[1:]) if d2 > d1])

def part_2():
    window_1 =[d1 + d2 + d3 for d1, d2, d3 in zip(depths, depths[1:], depths[2:])]
    window_2 = [d1 + d2 + d3 for d1, d2, d3 in zip(depths[1:], depths[2:], depths[3:])]
    # for x1, x2 in zip(window_1, window_2):
    #     print(x1, x2, "Increased" if x2 > x1 else "Decreased")
    return len([x1 for x1, x2 in zip(window_1, window_2) if x2 > x1])



if __name__ == '__main__':
    # print(part_1())
    print(part_2())

