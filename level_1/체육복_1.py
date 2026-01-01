def solution(n, lost, reserve):

    student = [1 for i in range(n)]
    for i in lost:  student[i-1] -= 1
    for i in reserve:   student[i-1] += 1
    
    for i, cloth in enumerate(student):
        if cloth == 0 and i > 0:
            if student[i-1] == 2:
                student[i-1] = 1
                student[i] = 1
        if cloth == 0 and i < n-1:
            if student[i+1] == 2:
                student[i+1] = 1
                student[i] = 1
    
    answer = 0
    for i in student: 
        if i > 0:
            answer += 1
    
    return answer
