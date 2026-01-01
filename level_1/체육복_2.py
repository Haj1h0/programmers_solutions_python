def solution(n, lost, reserve):
	
    u = [1] * (n + 2)
    for i in reserve:   u[i] += 1:
    for i in lost:      u[i] -= 1:
    
    for i in range(1, n + 1):
    	if u[i - 1] == 0 and u[i] == 2:
       		u[i - 1:i + 1] = [1, 1]
        elif u[i] == 2 and u[i + 1] == 0:
        	u[i:i + 2] = [1, 1]
            
    return len([x for x in u[1: -1] if x > 0])
    
# 맨 앞과 맨 뒤에 1을 한칸씩 추가
# 여벌을 가져온 학생 처리 : reserve의 길이에 비례, line 3
# 체육복을 잃어버린 학생 처리 : lost의 길이에 비례, line 4
# 체육복 빌려주기 처리 : 전체 학생 수 n에 비례 line 6
# 시간 복잡도 : O(n) linear time algorithm
