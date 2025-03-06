import sys

def generate_subsets():
    max_v = 0
    for i in range(1 << N):  # 2^N까지 반복
        subset = []
        skip = 0
        total = 0

        for j in range(N):
            if skip > 0:
                skip -= 1
                continue
            if i & (1 << j):
                T, P = arr[j]
                if j+T<=N:
                    total += P
                    skip = T - 1
                else:
                    break
            elif skip == 0:
                skip = 0

            max_v = max(max_v, total)

    return max_v

N = int(sys.stdin.readline())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

result = generate_subsets()
print(result)