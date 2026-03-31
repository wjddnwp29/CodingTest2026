def solution(s):
    k = list(map(int,s.split()))
    answer = f"{min(k)} {max(k)}"
    return answer