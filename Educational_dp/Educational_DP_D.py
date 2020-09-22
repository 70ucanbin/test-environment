N, W = map(int, input().split())
dp = [0] * (W + 1)
def dp_opt(n, w):
    for _ in range(N):
        w, v = map(int, input().split())
        for j in range(W, w-1, -1):
            tmp = dp[j-w] + v
            if tmp > dp[j]:
                dp[j] = tmp
    print(dp[-1])
dp_opt(N,W)