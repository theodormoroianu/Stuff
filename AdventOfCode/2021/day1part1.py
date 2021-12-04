import sys

data = [int(x) for x in sys.stdin.readlines()]

nr = len([i for i in range(1, len(data)) if data[i] > data[i - 1]])

print(nr)
