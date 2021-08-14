j, prev = 0, 0

def solution(servers, sticky, requests):
    answer = []
    for i in range(servers):
        answer.append(list())
    cnt = 0
    for i in range(len(requests)):
        global j, prev
        j, prev = 0, False
        if sticky:
            if i == 0:
                j = 0
            else:
                prev = (i + cnt) % servers
                if requests[i-1] == requests[i]:
                    j = (i - 1) % servers
                    cnt += 1
                else:
                    j = (i + cnt) % servers
        else:
            answer[i % servers].append(requests[i])
    return answer

print(solution(2, True, [1, 1, 2, 2]))