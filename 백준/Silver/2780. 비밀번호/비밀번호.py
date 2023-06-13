import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\BOJ\\input.txt", "r")

t = int(sys.stdin.readline())
# for i in near:
#     near_copy.append(i)

for _ in range(t):
    near = [0,
            2, 3, 2,
            3, 4, 3,
            3, 3, 2,
            1]
    near_copy = [1]*11
    near_copy[0] = 0
    n = int(sys.stdin.readline())

    if n == 1:
        print(10)
        continue
    if n == 2:
        print(sum(near))
        continue

    for _ in range(n-2):
        near_copy[1] = near[2]+near[4]
        near_copy[2] = near[1]+near[3]+near[5]
        near_copy[3] = near[2]+near[6]
        near_copy[4] = near[1]+near[5]+near[7]
        near_copy[5] = near[2]+near[4]+near[6]+near[8]
        near_copy[6] = near[3]+near[5]+near[9]
        near_copy[7] = near[4]+near[8]+near[10]
        near_copy[8] = near[5]+near[7]+near[9]
        near_copy[9] = near[6]+near[8]
        near_copy[10] = near[7]

        for i in range(len(near_copy)):
            near[i] = near_copy[i%1234567]

    #print(near_copy)
    print(sum(near_copy)%1234567)