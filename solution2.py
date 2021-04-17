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

# 강사님 코드(dp를 이용한 풀이)
def solution(land):
    dp = [[0 for _ in range(4)] for _ in range(2)]
    n = len(land)
    m = len(land[0])
    
    for i in range(n):
        for j in range(m):
            dp[i%2][j] = max(dp[(i-1)%2][:j] + dp[(i-1)%2][j+1:]) + land[i][j]
    
    return max(dp[(n-1)%2])