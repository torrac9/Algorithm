import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton04\\input.txt", "r")

t = int(sys.stdin.readline())

for _ in range(t):
    cnt = 1
    n = int(sys.stdin.readline())
    applicant = []
    for _ in range(n):
        applicant.append(list(map(int, sys.stdin.readline().split())))
    applicant.sort(key= lambda x: x[0])
    a = applicant[0][1]

    for i in range(1, n):
        if applicant[i][1] < a:
            a = applicant[i][-1]
            #print(applicant[i])
            cnt += 1


    #print(applicant)
    print(cnt)


    # new_applicant.sort(key= lambda x: x[1])
    # b = new_applicant[0][0]
    # for i in new_applicant:
    #     if i[0] > b:
    #         cnt += 1

    # a = applicant[-1][-1]

    # applicant.sort(key= lambda x: x[1])
    # b = applicant[-1][0]

    # new_applicant = [i for i in applicant if i[0] < b or i[1] < a]