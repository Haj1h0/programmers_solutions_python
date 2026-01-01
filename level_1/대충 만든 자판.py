def solution(keymaps, targets):
    km, answer = {}, []
    for keymap in keymaps:
        for i, v in enumerate(keymap, start = 1):
            if v not in km:
                km[v] = i
            elif v in km and km[v] > i:
                km[v] = i

    for target in targets:
        ans = 0
        for t in target:
            if t in km:
                ans += km[t]
            elif t not in km:
                ans = -1
                break
        answer.append(ans)

    return answer

"""
keymap을 value를 최소 눌러야 하는 횟수로 하는 dic로 구현, targets의 원소가 keymap.keys()에 포함되어 있지 않으면 -1
"""
