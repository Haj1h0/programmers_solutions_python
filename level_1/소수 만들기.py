import math

def p(n):
    if math.sqrt(n) % 1 == 0:
        return 0
    elif math.sqrt(n) % 1 != 0:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return 0
        return 1

def solution(nums):
    n, answer = len(nums), 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                answer += p(nums[i] + nums[j] + nums[k])
    return answer
