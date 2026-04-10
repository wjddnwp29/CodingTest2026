def solution(progresses, speeds):
    answer = []
    for i in range(len(speeds)):
        k = 100 - progresses[i]
        if k % speeds[i] == 0:
            answer.append(k//speeds[i])
        else:
            answer.append(k//speeds[i] + 1)
        
    
    answer2 = []
    front = answer[0]
    cnt = 0
    for i in answer:
        if i <= front:
            cnt+=1
        else:
            answer2.append(cnt)
            cnt=1
            front=i
    answer2.append(cnt)

    return answer2

