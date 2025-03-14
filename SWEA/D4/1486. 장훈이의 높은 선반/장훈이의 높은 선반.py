# 완전 탐색 할 필요는 x, 가능한 탑들 중 높이가 가장 낮은 탑을 구하기.
# 순열/조합으로 접근 시 모든 케이스를 확인하게 됨.??
# 순열 조합 부분집합 코드 다시 한 번 확인하자!!!!

# 각 점원 - 탑에 들어갈 지 아닐지 -> 포함 x, o인 경우 밖에 없음. 부분 집합 구하는 문제, 2**20 만큼 확인하게 됨. 약 백만번 확인.
# 재귀호출 이용한 부분 집합 확인 문제!

# level : 점원의 수. branch: 포함 유무 ox 두가지.
def recur(cnt, total_height):
    global answer
    # 기저조건 가지치기! 재귀 시 항상 확인해야 하는 조건.
    # 이미 B 이상인 경우 더 쌓을 필요가 없음. 기저조건 가지치기다..
    # 탑이 더 높은 정답은 필요 없다! B 이상일 때 최소값만 알면 됩니다..
    if total_height >= B:
        answer = min(answer, total_height)
        return
    if cnt == N:
        # 중단 조건
        return

    # 경우의 수 잘 그리기~~ 부분집합 어디에 포함 되느냐 안 되느냐는 간단하게 구현이 가능하다.
    # 두 가지 경우로 나누어 생각, 이를 위해 합을 같이 넘겨주자.
    recur(cnt + 1, total_height + heights[cnt])      # 포함 시키는 경우
    recur(cnt + 1, total_height)                                   # 포함 안 시키는 경우


T = int(input())
for tc in range(1,T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    # 정답: 탑의 높이, 차이
    answer = int(21e8)   # 21억. 매우 큰 수로 초기화 or 200001
    recur(0, 0)

    print(f'#{tc} {answer-B}')