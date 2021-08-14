import math


def solution(orderAmount, taxFreeAmount, serviceFee):
    # orderAmount : 주문금액
    # taxFreeAmount : 비과세금액
    # serviceFee : 봉사료
    answer = 0
    answer = math.ceil((orderAmount - serviceFee - taxFreeAmount)/11)
    if answer == 1:
        return 0
    return answer


print(solution(100, 0, 0))