from collections import deque

def solution(prices):
    q = deque(prices)
    answer = []

    while q:
        cnt = 0
        price = q.popleft()
        for w in q:
            cnt+=1
            


print(solution([1, 2, 3, 2, 3]))