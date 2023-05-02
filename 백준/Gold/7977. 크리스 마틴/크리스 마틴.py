import sys

n = int(sys.stdin.readline())
arr = sys.stdin.readline().strip()
a, c, g, t = 0, 0, 0, 0
min = 10000

for i in arr:
    if i == 'A':
        a += 1
    elif i == 'C':
        c += 1
    elif i == 'G':
        g += 1
    else:
        t += 1
if a < min:
    min = a
    min_index = 'A'
if c < min:
    min = c
    min_index = 'C'
if g < min:
    min = g
    min_index = 'G'
if t < min:
    min = t
    min_index = 'T'

print(min)
for _ in range(n):
    print(min_index, end='')