k = int(input())
now = 7

for i in range(1,k+1):
    tmp = now % k
    if tmp == 0:
        print(i)
        exit()
    else:
        now = tmp * 10 + 7
else:
    print(-1)