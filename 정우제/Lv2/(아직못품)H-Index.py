c = [3, 0, 6, 1, 5]	
c.sort(reverse=True)
print(c)
answer = 0
for i in range(len(c)):
    ## h-index 후보
    if (i+1) == c[i]:
        temp = sum(c[i+1::])
        ## 남은애들 개수가 h개라면...바로 return
        ## 아 남은애들 인용횟수가 h개 이하라면...
        if temp <= c[i]:
            answer = c[i]
            break
        ## 아니라면 pass
        else:
            pass

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        ## h-index 후보
        if (i+1) == citations[i]:
            temp = sum(citations[i+1::])
            ## 남은애들 개수가 h개라면...바로 return
            if temp <= citations[i]:
                answer = citations[i]
                break
            ## 아니라면 pass
            else:
                pass
    return answer