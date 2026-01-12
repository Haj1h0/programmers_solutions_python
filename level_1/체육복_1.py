# 오답 코드
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

# 틀린 이유
# 1. [0, 2, 0, 2 같은 경우 student[2] 번째에서 if 두개의 if문을 모두 돈다. 그렇기에 elif로 변경해주면 해결된다.
# 2. 하지만 elif로 변경해주어도 왼쪽이 못 빌려줘도 오른쪽을 아예 안 보는 버그가 생긴다. 
# 반례 : 초기 student = [1, 0, 2] / 정답은 3
# i=1에서 cloth=0, i>0라서 첫 if 진입, student[i-1] == 2는 거짓(왼쪽=1)이라 아무것도 안 함
# 그런데 elif는 스킵되어 오른쪽(2)을 확인하지 않음
# 결과: [1,0,2] 그대로 → 수업 가능 2명 → 오답

# 정답 코드
def solution(n, lost, reserve):
    
    # 전체 학생 수와 길이가 같은 student 리스트 
    # 체육복을 가져오지 못한 학생은 0, 여분의 체육복을 한벌 더 가져온 학생은 2, 본인의 체육복만 가져온 학생은 1로 구성
    student = [1 for i in range(n)]
    for i in lost:  student[i-1] -= 1
    for i in reserve:   student[i-1] += 1
    
    for i, cloth in enumerate(student):
        if cloth == 0:
            if i > 0 and student[i-1] == 2:
                student[i-1] = 1
                student[i] = 1              
            elif i < n-1 and student[i+1] == 2:
                student[i+1] = 1
                student[i] = 1
    
    answer = 0
    for i in student: 
        if i > 0:
            answer += 1
  
    return answer
