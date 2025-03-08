def previous_permutation(arr):
    i = len(arr) - 1
    # 뒤에서부터 첫 번째로 오름차순이 아닌 위치 찾기
    while i > 0 and arr[i - 1] <= arr[i]:
        i -= 1
    # 이미 가장 작은 순열이면 이전 순열이 없음
    if i <= 0:
        return False

    j = len(arr) - 1
    # arr[i-1]보다 작은 값 중 가장 오른쪽에 있는 원소 찾기
    while arr[j] >= arr[i - 1]:
        j -= 1

    # arr[i-1]과 arr[j] 교환
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # arr[i:]를 역순 정렬하여 이전 순열 완성
    arr[i:] = arr[len(arr) - 1 : i - 1 : -1]
    return True

n = int(input())
arr = list(map(int, input().split()))
if not previous_permutation(arr):
    print(-1)
else:
    print(' '.join(map(str, arr)))
