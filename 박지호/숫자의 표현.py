def solution(n):
    answer = 0
    start, end = 1,1
   
    while start < n and end < n:
        s=0
        for i in range(start,end+1):
            s+=i

        if s == n:
            answer+=1
            end += 1
            

        elif s < n:
            end+=1

        else :
            start+=1

    return answer

print(solution(15))

