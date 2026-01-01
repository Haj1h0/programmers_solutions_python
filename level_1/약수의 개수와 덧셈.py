import math

def solution(left, right):
    return sum([-i if math.sqrt(i) % 1 == 0 else i for i in range(left, right + 1)])

# 1 <= left <= right <= 1000
# 약수의 개수가 홀수인 경우는 그 수의 제곱근이 존재하는 경우

# for i in range(left, right+1):
#     if math.sqrt(i) % 1 == 0:     answer -= i
#     elif math.sqrt(i) % 1 != 0:   answer += i
