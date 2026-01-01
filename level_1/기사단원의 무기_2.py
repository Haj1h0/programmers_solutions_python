def cf(n): # 공약수 출력
    a = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            a.append(n//i)
            a.append(i)
    return len(set(a))                    # 제곱근이 자연수일 경우 자기 자신의 값이 2개가 들어가기에 set을 통해 해결해 준다.
  
def solution(number, limit, power):
    return sum([cf(i) if cf(i) <= limit else power for i in range(1,number+1)])
