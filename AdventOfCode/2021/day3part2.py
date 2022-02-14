import sys

lines = sys.stdin.read().split()

n = len(lines[0])

def get_number(l, t):
    for b in range(n):
        if len(l) == 1:
            return l[0]
        nr1 = len([row for row in l if row[b] == '1'])
        nr0 = len([row for row in l if row[b] == '0'])
        
        keep_bit = '1'
        if t == 'oxygen' and nr0 > nr1:
            keep_bit = '0'
        if t == 'co2' and nr0 <= nr1:
            keep_bit = '0'
        
        l = [row for row in l if row[b] == keep_bit]
    return l[0]


oxygen = get_number(lines, 'oxygen')
co2 = get_number(lines, 'co2')

print(oxygen, co2)

oxygen = int(oxygen, base=2)
co2 = int(co2, base=2)

print(f"oxygen = {oxygen}, co2 = {co2}, prod = {oxygen * co2}")
