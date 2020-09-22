# from itertools import product

# h, w, k = map(int, input().split())
# c = [list(input()) for _ in range(h)]

# ans = 0

# for row_bit in product(range(2), repeat=h):
#     for col_bit in product(range(2), repeat=w):
#         cnt = 0
#         for row in range(h):
#             for col in range(w):
#                 if c[row][col] == "#" and (row_bit[row] and col_bit[col]):
#                     cnt += 1
#         if cnt == k:
#             ans += 1

# print(ans)
h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]
 
ans = 0
for n in range(1 << h):
    for m in range(1 << w):
        cnt = 0
        for i in range(h):
            for j in range(w):
                if n>>i & 1: continue
                if m>>j & 1: continue
                if c[i][j] == '#': cnt += 1
        if cnt == k: ans += 1
 
print(ans)

