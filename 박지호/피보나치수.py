def solution(n):
    answer = 0
    a=0
    b=1
    for i in range(n-1):
        c = a + b
        a = b
        b = c
    return c % 1234567

print(solution(5))