import math

def solution(number, limit, power):
    answer = []
    for i in range(1, number + 1): 
        
        if math.sqrt(i) % 1 == 0:                         # 제곱근이 자연수로 존재하는 경우
            tmp = 1
            for j in range(1, int(math.sqrt(i))): 
                # TypeError: 'float' object cannot be interpreted as an integer, type(math.sqrt(i)) = float, ex) 1.0
                if i % j == 0:  tmp += 2

        elif math.sqrt(i) % 1 != 0:                       # 제곱근이 자연수로 존재하지 않는 경우
            tmp = 0
            for j in range(1, int(math.sqrt(i)) + 1):
                if i % j == 0:  tmp += 2
        answer.append(tmp)
        
    ans = [i if i <= limit else power for i in answer]
    return sum(ans)

# 수들에 대해 약수의 개수를 구하는 문제이다. 하지만 모든 수를 이중 for문을 통해 계산하면 O(n^2)로 시간 초과가 발생할 것이다.
# idea 1. 제곱근이 자연수로 존재하는 수들에 한해서는 ([1, 제곱근) 까지의 약수의 개수) * 2 + 1 을 한 결과와 같다.
# idea 2. 제곱근이 자연수로 존재하지 않는 수들에 한해서는 ([1, int(제곱근)] 까지의 약수의 개수) * 2 를 한 결과와 같다.
# idea 3. 엘라토스테네스의 체를 이용해 범위안 소수를 찾아 pass하고 확인한다. 
