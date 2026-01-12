def solution(answers):
    
    # 각각의 수포자들이 제출한 정답 list를 answer보다 큰 list로 만든다. 
    # 마지막 나머지 만큼을 각각의 수포자가 제출한 정답 list에서 이어붙여도 되지만 그렇지 않고 for문 통해 처리
    m1 = [1, 2, 3, 4, 5] * (len(answers)//5 + 1)
    m2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers)//8 + 1)
    m3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers)//10 + 1)
    a1, a2, a3 = 0, 0, 0
    
    # 각각의 수포자 1, 2, 3번의 정답과 answer을 zip을 통해 비교
    # 정답이 맞는 경우 각각의 a1, a2, a3 변수에 +1
    # answer 길이에 도달하면 break 통해서 for문 종료 
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
    
    # 가장 많은 정답을 맞춘 수포자를 출력
    # 최대 득점자가 중복되어도 if문에 동일하게 걸리기에 오름차순으로 출력됨
    answer = [i for i, a in enumerate(ans, start = 1) if a == max(ans)]
    return answer
