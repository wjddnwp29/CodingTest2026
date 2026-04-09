def solution(brown, yellow):
    
    answer = []
    for i in range(1,int(yellow**0.5) + 1):
        if yellow % i == 0:
            answer.append([yellow // i, i])

    for i,j in answer:
        if 2*i + 2*j + 4 == brown:
            return [i+2,j+2]
    