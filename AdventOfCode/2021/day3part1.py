import sys

lines = sys.stdin.read().split()

n = len(lines[0])

print(n)
print(lines)

nr = 0

for i in range(n):
	bits = [l[i] for l in lines]
	bits = sorted(bits)
	b = bits[len(bits) // 2]
	if b == '1':
		nr += (1 << (n - i - 1))

nr2 = (1 << n) - 1 - nr

print(f"Nr = {nr}, nr2 = {nr2}, prod = {nr * nr2}")


