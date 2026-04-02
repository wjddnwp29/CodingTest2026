def solution(n):
    arr = bin(n)[2:]
    c_1 = arr.count("1")
    c1_1 = 0
    i = 0
    while c1_1 != c_1:
        i += 1
        arr1 = bin(n+i)[2:]
        c1_1 = arr1.count("1")
        
    return n+i

print(solution(15))