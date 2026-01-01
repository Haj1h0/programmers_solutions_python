def solution(s):
    al, answer = {}, []
    for i, a in enumerate(s):
        if a not in al:
            al[a] = i
            answer.append(-1)
        elif a in al:
            answer.append(i - al[a])
            al[a] = i   
    
    return answer
