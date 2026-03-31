'''JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.'''

def solution(s):
    answer = s.split()
    answer2 = ""
    for i in range(len(answer)):
        temp = ""
        ## 알파벳일때 처리
        if answer[i][0].isalpha():
            temp += answer[i][0].upper()
        elif answer[i][0] == " ":
            temp += " "
        ## 숫자 처리
        else:
            temp += answer[i][0]
            
        for j in range(1, len(answer[i])):
            ## 알파벳일떄 처리
            if answer[i][j].isalpha():
                temp += answer[i][j].lower()
            elif answer[i][j] == " ":
                temp += " "
            ## 아닐때 처리
            else:
                temp += answer[i][j]
        if i == len(answer) - 1:
            answer2 += temp
        else:
            answer2 += temp + " "
    return answer2

print(solution(" "))


