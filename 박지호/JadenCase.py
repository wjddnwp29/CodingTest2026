def solution(s):
    k = s.split(' ')
    for i in range(len(k)):
        k[i] = k[i].capitalize()
    answer = ' '.join(k)
    return answer