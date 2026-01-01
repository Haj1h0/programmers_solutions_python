from string import ascii_lowercase
def solution(s, skip, index):
    result = ''

    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    l = len(a_to_z)

    dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}

    for i in s:
        result += a_to_z[(dic_alpha[i] + index) % l]

    return result


"""
def solution(s, skip, index):
    alphas = [chr(a) for a in range(ord("a"), ord("z")+1) if chr(a) not in skip]
    return "".join([alphas[(alphas.index(a) + index) % len(alphas)] for a in s])
"""
