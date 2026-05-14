def solution(citations):
    citations.sort()

    for i in range(len(citations)):
        temp = citations[i]
        if len(citations[i+1::]) <= i:
            return citations[i]
    return 0


citations = [3,0,6,1,5]
## 얘로 정렬하고...
citations.sort()

for i in range(len(citations)):
    temp = citations[i]
    if len(citations[i+1::]) <= i:
        print(citations[i])
        
print(solution([1,1]))