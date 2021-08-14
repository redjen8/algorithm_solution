def solution(input):
    res = ""
    M, N = map(int, input().split())
    print(M, N)
    exposeList= [0] * 10000
    day = 0
    dueDate = -1
    while True:
        ipt = input()
        if ipt == "SHOW":
            lb = 0
            if day >= M:
                lb = day - M
            totalTry = 0
            for i in range(lb, day+1):
                totalTry += exposeList[i]
            if totalTry >= N:
                dueDate = day + M
            if day < dueDate:
                print(0)
            else:
                exposeList[day] += 1
                print(1)
        elif ipt == "NEGATIVE":
            dueDate = day + M
            print(0)
        elif ipt == "NEXT":
            day += 1
            print('-')
        elif ipt == "EXIT":
            print("BYE")
            exit(0)
        else:
            print("ERROR")
