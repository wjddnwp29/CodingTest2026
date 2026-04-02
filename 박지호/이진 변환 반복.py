def solution(s):
    cnt=0
    zeros = 0
    
    while s != "1":
        cnt+=1
        zeros += s.count('0')
        c = len(s) - s.count('0')
        s = bin(c)[2:]

    return [cnt, zeros]