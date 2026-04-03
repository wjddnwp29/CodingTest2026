def solution(brown, yellow):
    
    answer = [i for i in range(1,yellow+1) if yellow % i ==0]
    mid = len(answer) // 2

    k1 = answer[mid]
    k2 = yellow / k1
    
    return [k2+2,k1+2]
print(10,2)