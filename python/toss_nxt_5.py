def solution(fruitWeights, k):
    answer = set()
    for i in range(len(fruitWeights)-k+1):
        rangeFruit = fruitWeights[i:i+k]
        answer.add(max(rangeFruit))
    answer = list(answer)
    answer.sort(reverse=True)
    return answer


print(solution([30, 40, 10, 20, 30], 3))