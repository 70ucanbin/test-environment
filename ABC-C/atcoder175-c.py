X, K, D = map(int, input().split())
X = abs(X)
if D * K > X:
    if (K - X // D )% 2 == 0:
        print(X - D * (X // D))
    else:
        print(abs(X - D * (X // D) - D))
else:
    print(X - D * K)