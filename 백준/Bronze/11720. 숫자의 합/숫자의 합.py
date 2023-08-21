import sys
#sys.stdin = open("C:/Users/82103/Desktop/KraftonJungle/BOJ/input.txt", "r")

n = int(sys.stdin.readline())
nums = sys.stdin.readline().strip()
sol = 0

for i in nums:
    sol += int(i)

print(sol)