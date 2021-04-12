def solution(land):
    answer = 0
    before_index = None;
    for i in range(3):
        if i > 0:
            before_index = land[i-1].index(max(land[i-1]))
        if before_index != None and before_index == land[i].index(max(land[i])):
            land[i].pop(before_index)
            answer += max(land[i])
        else:
            answer += max(land[i])
    return answer
