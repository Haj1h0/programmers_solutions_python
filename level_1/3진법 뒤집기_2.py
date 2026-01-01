def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
	# tmp 문자열을 3진수로 만들기
	return answer
