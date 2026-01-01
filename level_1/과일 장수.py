def solution(k, m, score):
    score.sort(reverse = True)
    return sum([score[i] * m if len(score) >= m else 0 for i in range(m-1,len(score),m)])
