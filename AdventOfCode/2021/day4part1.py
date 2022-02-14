import sys

numbers = sys.stdin.readline().split(',')
numbers = [int(x) for x in numbers]

rest_of_input = sys.stdin.read().splitlines()
rest_of_input = [[int(x) for x in row] for row in rest_of_input]

bingos = [rest_of_input[i:i+5] for i in range(1, len(rest_of_input), 6)]


def win_score(bingo) -> Tuple[int, int]:



