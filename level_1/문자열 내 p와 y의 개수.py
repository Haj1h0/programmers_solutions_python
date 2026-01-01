def solution(s):
    s = list(s)
    if not('p' in s or 'P' in s or 'y' in s or 'Y' in s):
        return True
    elif s.count('P') + s.count('p') != s.count('y') + s.count('Y'):
        return False
    else:
        return True

# def numPY(s):
#    return s.lower().count('p') == s.lower().count('y')
