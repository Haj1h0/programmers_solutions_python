def solution(phone_number):
    ans = ['*' for i in range(0, len(phone_number)-4)]
    return ''.join(ans) + phone_number[-4:]

"""
def hide_numbers(s):
    return "*" * (len(s) - 4) + s[-4:]
    # 문자열에 곱 연산 가능
"""
