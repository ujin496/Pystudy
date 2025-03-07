# 그냥 리스트 append(), pop() 사용하기
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack_num = []    # 비교할 수 저장할 스택
stack_idx = []    # 그 수의 인덱스 저장할 스택

for i in range(n):
    if not stack_idx:    # 스택이 비어있으면 현재 수 스택에 넣어서 다음 수와 비교
        stack_num.append(arr[i])
        stack_idx.append(i)

    elif arr[i] <= stack_num[-1]:    # 현재 수가 스택에 저장된 수보다 크지 않으면 스택에 넣기
        stack_num.append(arr[i])
        stack_idx.append(i)

    else:    # 현재 수가 스택에 저장된 수보다 크면 저장된 인덱스에 접근해 현재 수로 모두 바꿔버림
        while stack_idx and stack_num[-1] < arr[i]:
            arr[stack_idx.pop()] = arr[i]
            stack_num.pop()
        stack_num.append(arr[i])    # 현재 수를 스택에 넣어서 다음 수와 비교
        stack_idx.append(i)

while stack_idx:    # 스택에 남아있는 수의 인덱스에 접근해 -1로 만들기
    arr[stack_idx.pop()] = -1

print(*arr)
