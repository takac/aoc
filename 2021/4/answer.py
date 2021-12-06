from typing import List, Tuple

NumberBoard = List[List[int]]
MarkBoard = List[List[bool]]

def load_puzzle() -> Tuple[List[int], List[NumberBoard]]:
    content = open("input").read().strip()
    nums_str, rest = content.split("\n", 1)
    nums = [int(i) for i in nums_str.split(",")]
    boards = [
        [
            [int(n.strip()) for n in line.split(" ") if n.strip()]
            for line in board.split("\n")
            if line.strip()
        ]
        for board in rest.split("\n\n")
    ]
    return nums, boards

def check_complete(mark_board: MarkBoard) -> bool:
    return any(all(row) for row in mark_board) or any(all(col) for col in zip(*mark_board))

def update_mark_board(num: int, number_board: NumberBoard, mark_board: MarkBoard) -> None:
    print(f'check for {num} in {number_board}')
    for i in range(5):
        for j in range(5):
            if number_board[i][j] == num:
                # print(number_board)
                print("Update", i, j, number_board[i][j], number_board[i])
                mark_board[i][j] = True
                return

def create_mark_board() -> MarkBoard:
    return [[False for j in range(5)] for i in range(5)]

def get_unmarked_sum(number_board: NumberBoard, mark_board: MarkBoard) -> int:
    total = 0
    for i in range(5):
        for j in range(5):
            if mark_board[i][j] is False:
                total = total + number_board[i][j]
    return total

def run_game():
    # print(load_puzzle())
    nums, number_boards = load_puzzle()
    numbers_marks = [(num_board, create_mark_board()) for num_board in number_boards]
    # print(create_mark_board())
    for n in nums:
        print(n)
        print(numbers_marks)
        for nb, mb in numbers_marks:
            update_mark_board(n, nb, mb)
            if check_complete(mb):
                print(f"COMPLETE: {n}")
                unmarked_sum = get_unmarked_sum(nb, mb)
                print(unmarked_sum * n)
                return

    print(numbers_marks)

def find_last_board_to_win():
    nums, number_boards = load_puzzle()
    numbers_marks = [(num_board, create_mark_board()) for num_board in number_boards]
    original_nm = [(num_board, create_mark_board()) for num_board in number_boards]

    for n in nums:
        for nb, mb in numbers_marks.copy():
            update_mark_board(n, nb, mb)
            if check_complete(mb):
                if len(numbers_marks) == 1:
                    print(f"COMPLETE: {n}")
                    unmarked_sum = get_unmarked_sum(nb, mb)
                    print(unmarked_sum)
                    print(unmarked_sum * n)
                    return
                else:
                    numbers_marks.remove((nb, mb))


if __name__ == "__main__":
    # run_game()
    find_last_board_to_win()
