n = int(input())
A = list(map(int, input().split()))
ans = 0
p = A[0]
for i in range(1,n):
    if A[i] < p:
        ans += p - A[i]
    else:
        p = A[i]
print(ans)