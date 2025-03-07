def solve(word, n):
    if n == 1:
        return "NO"
    else:
        for i in range(1, n):
            left = word[:i]
            right = word[i:]
            left_sum = 1
            right_sum = 1
            for j in left:
                left_sum *= int(j)
            for k in right:
                right_sum *= int(k)
            if left_sum == right_sum:
                return "YES"
        else:
            return "NO"


num = input()
n = len(num)
result = solve(num, n)
print(result)
