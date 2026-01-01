def solution(sizes):
    for size in sizes:
        size.sort()
    return max(map(lambda x : x[1], sizes)) * max(map(lambda x : x[0], sizes))


# def solution(sizes):
#     return max(max(x) for x in sizes) * max(min(x) for x in sizes)
