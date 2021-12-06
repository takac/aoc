from typing import List, Dict
from collections import Counter, defaultdict


def get_initial_state() -> List[int]:
    return [int(i) for i in open("input").read().strip().split(",")]


def iterate_buckets(state: Dict[int, int]) -> Dict[int, int]:
    new_counter = defaultdict(int)
    for k, v in state.items():
        k = k - 1
        if k == -1:
            new_counter[8] = v
            new_counter[6] = new_counter[6] + v
        else:
            new_counter[k] = new_counter[k] + v
    return new_counter


if __name__ == "__main__":
    state = Counter(get_initial_state())
    print("Initial state:", ",".join(str(n) for n in state))
    for i in range(256):
        state = iterate_buckets(state)
        count = sum(v for v in state.values())
        print(f"After {i+1} days: Len: {count}")
