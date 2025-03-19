def check(row, col):
    # 같은 열에 말이 놓여 있을 경우
    for i in range(row):
        if visited[i][col]:
            return False
    # 왼쪽 대각선에 말이 놓여 있을 경우
    i, j = row-1, col-1
    # 방문 체크 배열의 index out of range 방지
    while i >= 0 and j >= 0:
        if visited[i][j]:
            return False
        i -= 1
        j -= 1
    # 오른쪽 대각선에 말이 놓여 있을 경우
    i, j = row-1, col+1
    while i >= 0 and j < N:
        if visited[i][j]:
            return False
        i -= 1
        j += 1
    # 모든 안 되는 경우의 수 검사를 마쳤을 경우 놓여도 되는 곳
    return True

# level: N개의 행
# branch: 선택 가능한 요소 - N개의 열
def dfs(row):
    global answer
    if row == N:
        answer += 1
        return
    for col in range(N):
        if check(row, col) is False:    # 만약 둘 수 없는 곳이라면 반복문 해당 회차 pass
            continue
        visited[row][col] = 1
        dfs(row + 1)
        visited[row][col] = 0       # 백트래킹

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    answer = 0
    visited = [[0] * N for _ in range(N)]
    dfs(0)

    print(f'#{tc} {answer}')