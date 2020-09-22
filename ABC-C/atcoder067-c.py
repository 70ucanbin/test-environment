# N 枚のカードに書かれた数の総和を X とする．
# カードの山の先頭 i 枚のカードに書かれた数の総和が xi であったとすると，
# 残ったカードたちに書かれた数の和 yi は X − xi であり，
# |yi − xi|は |X − 2xi| となる．1 から N − 1 までの全ての i について |X − 2xi| を試せばよい．
# これは O(N) で実行可能であり，十分高速である．

# n=int(input())
# a=list(map(int,input().split()))
# X=sum(a)
# ans=10**9
# for i in range(1,n):
#     ans=min(ans,abs(X - 2*sum(a[:i])))
# print(ans)
# ↑は間に合わない　恐らくsum(a[:i])の処理で時間がかかってる


n=int(input())
a=list(map(int,input().split()))
ans=10**100
x=sum(a)
b=0
for i in a[:-1]:
   b+=i
   x-=i
   ans=min(ans,abs(x-b))
print(ans)