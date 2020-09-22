# n,k = map(int,input().split())
# d = {}
# for _ in range(n):
#     a,b = map(int,input().split())
#     d[str(a)] = d.get(str(a),0) +b
# d2 = sorted(d.items(), key=lambda x: x[0])
# cnt=0
# for i in d2:
#     cnt+=i[1]
#     if cnt >= k:
#         print(int(i[0]))
#         exit(0)

n,k=map(int,input().split())
x=[0]*(10**5)#1~10**5
for i in range(n):
    a,b=map(int,input().split())
    x[a-1]+=b
for i in range(10**5):
    k-=x[i]
    if k<=0:
        print(i+1)
        break