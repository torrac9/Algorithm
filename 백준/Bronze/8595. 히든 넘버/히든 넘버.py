import sys
#sys.stdin = open("C:/Users/82103/Desktop/KraftonJungle/BOJ/input.txt", "r")

n = int(sys.stdin.readline())
hidden = sys.stdin.readline().strip()
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
arr = []
sol = []
result = 0

for i in range(len(hidden)):
    if hidden[i] in nums:
        arr.append(int(hidden[i]))
    else:
        sol.append(arr)
        arr = []
sol.append(arr)
for i in sol:
    if i:
        for j in range(len(i)):
            result += i[j] * 10**(len(i) - j-1)
#print(sol)
print(result)