A,B,C,D,E,F = map(int, input().split())

x = sorted(set([w for i in range(0,F+1,A*100) for j in range(0,F+1,B*100) if (w := i + j) < F]))[1::]
y = sorted(set([s for i in range(0,F+1,C) for j in range(0,F+1,D) if (s := i + j) < F]))

n = 0
WS = S = 0
for w in x:
    for s in y:
        if w + s > F:
            break
        if w * E//100 >= s:
            m = s / (w + s)
            if m >= n:
                n = m
                WS, S = w + s , s

print(WS,S)
