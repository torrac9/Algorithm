def solution(today, terms, privacies):
    y, m, d = today.split('.')
    y = int(y)
    m = int(m)
    d = int(d)
    term = []
    privacy= []
    sol = []
    for i in terms:
        a, b = i.split(' ')
        term.append([a, int(b)])
    for i in range(len(privacies)):
        t, ab = privacies[i].split(' ')
        yy, mm, dd = t.split('.')
        privacy.append([ab, int(yy), int(mm), int(dd), i+1])
    
    for i in privacy:
        for j in term:
            if i[0] == j[0]:
                i[2] += j[1]
                if i[2] > 12:
                    if i[2]%12 != 0:
                        i[1] += i[2]//12
                        i[2] = i[2]%12
                    else:
                        i[1] += i[2]//12 -1
                        i[2] = 12

        
        #print(i)
        if i[1] < y:
            sol.append(i[4])
        elif i[1] == y and i[2] < m:
            sol.append(i[4])
        elif i[1] == y and i[2] == m and i[3] <= d:
            sol.append(i[4])
    
    #print(sol)
    return sol