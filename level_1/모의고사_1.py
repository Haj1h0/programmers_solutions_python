def solution(answers):
    m1 = [1, 2, 3, 4, 5] * (len(answers)//5 + 1)
    m2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers)//5 + 1)
    m3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers)//5 + 1)
    a1, a2, a3 = 0, 0, 0
  
    for i, z in enumerate(zip(m1, answers), start = 1):
        if z[0] == z[1]:
            a1 += 1
        if i == len(answers):
            break
    for i, z in enumerate(zip(m2, answers), start = 1):
        if z[0] == z[1]:
            a2 += 1
        if i == len(answers):
            break
    for i, z in enumerate(zip(m3, answers), start = 1):
        if z[0] == z[1]:
            a3 += 1
        if i == len(answers):
            break
          
    ans = [a1, a2, a3]
    answer = [i for i, a in enumerate(ans, start = 1) if a == max(ans)]
    return answer
