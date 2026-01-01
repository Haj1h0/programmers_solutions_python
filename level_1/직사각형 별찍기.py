a, b = map(int, input().strip().split(' '))
for i in range(b):
    print('*' * a)


# answer = ('*' * a + '\n') * b


"""
a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print('*', end='')
    print('')
"""
