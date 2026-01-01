def solution(numbers):

    numbers_str = [str(i) for i in numbers]
    numbers_str.sort(key = lambda x : int((x * 4)[0:4]), reverse = True)
    # numbers_str.sort(key = lambda x : (x * 4)[0:4]), reverse = True)
    # 문자열은 사전의 순서를 따르고 숫자가 들어간 문자열에 관해서는 작은 순 부터 정렬을 
    # 진행하기에 int를 적지 않아도 된다.
    
    answer = ''
    if numbers_str[0] == '0':	# [0, 0] 일 경우 return 값이 "00"으로 나온다.
        return '0'
    else:
        for i in numbers_str:
            answer += i
        # answer = "".join(numbers_str)
            
    return answer
