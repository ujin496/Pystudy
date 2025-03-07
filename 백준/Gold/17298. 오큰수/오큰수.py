import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack_num = [0] * n    # 비교할 수 저장할 스택
stack_idx = [0] * n    # 그 수의 인덱스 저장할 스택
top = -1

for i in range(n):
    if top == -1:    # 스택이 비어있으면 현재 수 스택에 넣어서 다음 수와 비교
        top += 1
        stack_num[top], stack_idx[top] = arr[i], i

    elif arr[i] <= stack_num[top]:    # 현재 수가 스택에 저장된 수보다 크지 않으면 스택에 넣기
        top += 1
        stack_num[top], stack_idx[top] = arr[i], i

    else:    # 현재 수가 스택에 저장된 수보다 크면 저장된 인덱스에 접근해 현재 수로 모두 바꿔버림
        while stack_num[top] < arr[i] and top > -1:
            arr[stack_idx[top]] = arr[i]
            top -= 1
        top += 1    # 현재 수를 스택에 넣어서 다음 수와 비교
        stack_num[top], stack_idx[top] = arr[i], i

while top > -1:    # 스택에 남아있는 수의 인덱스에 접근해 -1로 만들기
    arr[stack_idx[top]] = -1
    top -= 1

print(*arr)
