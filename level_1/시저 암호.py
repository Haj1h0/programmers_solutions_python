def solution(s, n):
    # a = 97, z = 122, A = 65, Z = 90
    answer = ''
    for i in s:
        if i == " ":
            answer += " "
        elif ord(i) >= 97 and ord(i) <= 122:
            if ((ord(i) + n) % 122) > 0 and ((ord(i) + n) % 122) < 97:
                answer += chr(((ord(i) + n) % 122) + 96)
            else:
                answer += chr(ord(i)+n)
        elif ord(i) >= 65 and ord(i) <= 90:
            if ((ord(i) + n) % 90) > 0 and ((ord(i) + n) % 90) < 65:
                answer += chr(((ord(i) + n) % 90) + 64)
                print(ord(i)+n)
            else:
                answer += chr(ord(i)+n)

    return answer
