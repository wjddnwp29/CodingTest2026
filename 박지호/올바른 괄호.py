def solution(s):
    answer = True
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        elif s[i] == ")":
            if not stack :
                answer = False
                break
                
            P = stack.pop()        
            if s[i] == ")" and P == "(":
                answer = True
            else:
                answer = False

    if stack :
        answer = False        
    return answer