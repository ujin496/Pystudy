def solve(N):
    for c in range(1, len(N)):  # c: 구역 나눌 범위
        front = 1       # 곱셈이므로 초기값은 1
        back = 1
        
        for i in range(c):  # fromt 구간 요소 곱해주기
            front *= int(N[i])
        for i in range(c, len(N)):  # back 구간 요소 곱해주기
            back *= int(N[i])
        
        if front == back:
            return "YES"
    
    return "NO"

N = input()
print(solve(N))