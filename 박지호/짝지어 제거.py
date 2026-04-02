def solution(s):
    i=0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            s = s[:i] + s[i+2:]
            i=0
        else : 
            i+=1

    if not s : k=1
    else : k=0
    return k

print(solution("cdcd"))