def solution(k, score):
    a, answer = [], []
    for i, s in enumerate(score, start = 1):
        if i <= k:
            a.append(s) 
            a.sort()
        elif i > k:
            if s > a[0]:
                a.append(s)
                del a[0]
                a.sort()

        answer.append(a[0])  
    return answer
