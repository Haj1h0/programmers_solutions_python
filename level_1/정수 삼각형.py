def solution(triangle):
    triangle.reverse()

    for i, t in enumerate(triangle, start = 1):
        if len(t) > 1:
            for k in range(len(t)-1):
                triangle[i][k] += max(t[k],t[k+1])

        elif len(t) == 1:
            return t[0]
