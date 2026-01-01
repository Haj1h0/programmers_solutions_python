def solution(s):
    ans = []
    for i in s.split():
        if i != "Z":
            ans.append(i)
        else:
            ans.pop()
    
    return sum(list(map(int, ans)))
