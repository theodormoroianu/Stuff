import sys

ops = sys.stdin.readlines()

dep, hor = 0, 0

for op in ops:
	t, nr = op.split()
	nr = int(nr)
	if t == "forward":
		hor += nr
	elif t == "down":
		dep += nr
	elif t == "up":
		dep -= nr
	else:
		raise Exception("WFT")

print(dep, hor, ", prod =", dep * hor)

