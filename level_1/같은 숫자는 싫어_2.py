def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
    
 # 빈 리스트의 [-1]에 접근하기 위해 슬라이싱을 사용한다.
