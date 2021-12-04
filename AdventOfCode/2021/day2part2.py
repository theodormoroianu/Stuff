import sys

ops = sys.stdin.readlines()

dep, hor, aim = 0, 0, 0

for op in ops:
	t, nr = op.split()
	nr = int(nr)
	if t == "forward":
		hor += nr
		dep += aim * nr
	elif t == "down":
		# dep += nr
		aim += nr
	elif t == "up":
		# dep -= nr
		aim -= nr
	else:
		raise Exception("WFT")

print(dep, hor, ", prod =", dep * hor)

