def solution(s, skip, index):
    a, answer = "abcdefghijklmnopqrstuvwxyz", []
    alphabet = [i for i in a if i not in skip]
    for i in s:
        if alphabet.index(i) + index <= len(alphabet) - 1:
            answer.append(alphabet[alphabet.index(i) + index])
        else:
            answer.append(alphabet[(alphabet.index(i) + index) % len(alphabet)])
        #   answer.append(alphabet[alphabet.index(i) + index - len(alphabet)])
        #   '-'로 작성 시 런타임 에러, alphabet list를 한번 이상 도는 경우 인덱스를 잘못 참조하게 된다.
    return "".join(answer)
