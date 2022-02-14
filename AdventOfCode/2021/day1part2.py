import sys

data = [int(x) for x in sys.stdin.readlines()]

nr = len([i for i in range(3, len(data)) if data[i] > data[i - 3]])

print(nr)
