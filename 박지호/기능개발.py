def solution(progresses, speeds):
    answer = []
    for i in range(len(speeds)):
        k = 100 - progresses[i]
        if k % speeds[i] == 0:
            answer.append(k//speeds[i])
        else:
            answer.append(k//speeds[i] + 1)
        
    cnt = 1
    answer2 = []
    while answer:
        if len(answer) == 1:
            answer2.append(cnt)
            break
        if answer.pop() > answer[-1]:
            answer2.append(cnt)
            cnt=1
        else :
            cnt += 1

    return answer2[::-1]

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))