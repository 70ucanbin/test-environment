N,T=map(int,input().split())
t= list(map(int,(input().split())))
print(sum([min(t[i]-t[i-1],T) for i in range(1, N)])+T)