def solution(A,B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    answer=0
    for i in range(len(A)):
        if A[0]>B[0]:
            answer += A.pop(0) * B.pop()
        else:
            answer += A.pop() * B.pop(0)
        

    return answer