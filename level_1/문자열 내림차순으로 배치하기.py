def solution(s):
    return "".join(sorted(s, key = lambda x: ord(x), reverse = True))
   	# return "".join(sorted(s, reverse=True))
    # 문자 자체도 순서 존재
