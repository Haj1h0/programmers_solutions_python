def solution(arr):
    answer = [num for i, num in enumerate(arr) if i <= len(arr)-2 and arr[i+1] != num]
    answer.append(arr[-1])    
    return answer
