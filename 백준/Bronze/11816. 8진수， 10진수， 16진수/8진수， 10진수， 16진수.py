import sys
#sys.stdin = open("C:/Users/82103/Desktop/KraftonJungle/BOJ/input.txt", "r")

x = sys.stdin.readline().strip()
sol = 0

if x[0] == "0":
    if x[1] == "x":
        for i in range(len(x[2:])):
            if x[2+i] == "f":
                sol += 15 * 16**(len(x[2:]) - i-1)
            elif x[2+i] == "e":
                sol += 14 * 16**(len(x[2:]) - i-1)
            elif x[2+i] == "d":
                sol += 13 * 16**(len(x[2:]) - i-1)
            elif x[2+i] == "c":
                sol += 12 * 16**(len(x[2:]) - i-1)
            elif x[2+i] == "b":
                sol += 11 * 16**(len(x[2:]) - i-1)
            elif x[2+i] == "a":
                sol += 10 * 16**(len(x[2:]) - i-1)
            else:
                sol += int(x[2+i]) * 16**(len(x[2:]) - i-1)
    else:
        for i in range(len(x[1:])):
            sol += int(x[1+i]) * 8**(len(x[1:]) -i-1)
else:
    sol = int(x)


print(sol)