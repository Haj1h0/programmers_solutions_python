def solution(food):
    a = "".join([str(i) * (f//2) for i, f in enumerate(food[1:], start = 1) if f//2 > 0])
    return a + "0" + a[::-1]

"""
string reverse
s = 'Reverse this strings'
1. reversed(s) # 반전된 오브젝트
''.join(s) 
2. s[::-1]
"""
