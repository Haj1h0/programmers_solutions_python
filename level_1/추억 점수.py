def solution(name, yearning, photo):
    h = {}
    answer = []
    
    # h = dict(zip(name,yearing))
    for i, nm in enumerate(name):
        h[nm] = yearning[i]
       
    for i in photo:
        ans = 0
        for j in i:
            if j in h.keys():	# if j in h: dic는 for문 통해 돌리면 key값 할당됨
                ans += h[j]
        answer.append(ans)
    return answer
