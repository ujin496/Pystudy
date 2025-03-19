def find_set(x):
    while rep[x] != x:
        x = rep[x]
    return x

def union(x,y):
    rep[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    rep = [i for i in range(N+1)]
    for i in range(M):
        a,b = arr[2*i], arr[2*i+1]
        union(a,b)

    # print(f'#{tc} {len(set(rep))-1}')
    # 대표 원소 찾기 -> rep[x] = x인 경우
    cnt = 0
    for i in range(1,N+1):
        if rep[i] == i:
            cnt += 1
    print(f'#{tc} {cnt}')