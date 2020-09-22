# 全探索
n = int(input())
arr = [list(map(int,input().split())) for _ in range(2)]
ans = 0
for i in range(n):
    ans = max(ans, sum(arr[0][:i+1] + arr[1][i:]))
else:
    print(ans)

# dp解
# n = int(input())
# a = [list(map(int,input().split())) for _ in range(2)]
# s = 0
# for i in range(n):
#     s += a[0][i]
#     a[0][i] = s
# a[1][0] += a[0][0]
# for i in range(1, n):
#     a[1][i] += max(a[0][i], a[1][i - 1])
# print(a[1][-1])