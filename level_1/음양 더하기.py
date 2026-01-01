def solution(absolutes, signs):
    return sum([absolutes[i] if signs[i] else -absolutes[i] for i in range(len(absolutes))])


# def solution(absolutes, signs):
#     return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
