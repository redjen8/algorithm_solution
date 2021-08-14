import re

def solution(amountText):
    if amountText.find(',') != -1:
        regA = re.compile(r'([1-9]){1}(\d{,2}(,\d{3})*$)')
        if regA.match(amountText):
            answer = True
        else:
            answer = False
    else:
        regB = re.compile(r'([1-9])+\d*')
        if regB.match(amountText):
            if amountText[0] != '0':
                answer = True
            else:
                answer = False
        else:
            answer = False
    return answer

print(solution("0,112,333")) 