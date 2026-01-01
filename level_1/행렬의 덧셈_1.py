import numpy as np

def solution(arr1, arr2):
    ret1 = np.array(arr1)
    ret2 = np.array(arr2)
    answer = ret1 + ret2
    return answer.tolist()
