# 必要な情報は一日前までの、a,b,cそれぞれ選択時の最大幸福値
# iがa,b,cのそれぞれのi-1のa,b,cの最大値を加算すればOK

n = int(input())
event = []
for _ in range(n):
    event.append(list(map(int,input().split())))

dp = [[0] * 3 for i in range(n)]
dp[0] = event[0]

for i in range(1,n):
    for j in range(3):
        dp[i][j] = max([event[i][j] + dp[i-1][k] for k in range(3) if k != j])

print(max(dp[-1]))