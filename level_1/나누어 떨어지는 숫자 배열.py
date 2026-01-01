def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    if answer:
        return sorted(answer)
    else:
        return [-1]

# def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
# A or B -> if True: A, else: B
# empty list == False
