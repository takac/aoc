from typing import List
from statistics import median

def get_positions() -> List[int]:
    return [int(i) for i in open("input").read().split(",")]

# def get_fuel_cost(positions: List[int], choice: int):
if __name__ == "__main__":
    positions = get_positions()
    print(positions)
    print(len(positions))
    med = int(median(positions))
    s = sum([abs(p - med) for p in positions])
    print(s)
    # part 2
    nat = lambda n: (n * (n+1))//2
    print(
        min(
            sum(nat(abs(i - pos)) for pos in positions)
            for i in range(max(positions))
        )
    )

    # print(sum(nat(abs(5 - pos)) for pos in positions))
