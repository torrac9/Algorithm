def solution(answers):
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score1 = 0
    score2 = 0
    score3 = 0
    s1 = 0
    for i in range(len(answers)):
        if s1 > 4:
            s1 -= 5
        if answers[i] == supo1[s1]:
            score1 += 1
        s1 += 1
    s2 = 0
    for i in range(len(answers)):
        if s2 > 7:
            s2 -= 8
        if answers[i] == supo2[s2]:
            score2 += 1
        s2 += 1
    s3 = 0
    for i in range(len(answers)):
        if s3 > 9:
            s3 -= 10
        if answers[i] == supo3[s3]:
            score3 += 1
        s3 += 1
    ms = max(score1, score2, score3)
    arr = []
    if ms == score1:
        arr.append(1)
    if ms == score2:
        arr.append(2)
    if ms == score3:
        arr.append(3)
    return arr