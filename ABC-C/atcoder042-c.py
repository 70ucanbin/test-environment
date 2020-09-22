n,_ = map(int,input().split())
d = list(input().split())
flg=True
while flg:
    flg=False
    for i in str(n):
        if i in d:
            flg=True
            n+=1
            break
print(n)