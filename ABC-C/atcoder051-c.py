sx, sy, tx, ty = map(int, input().split())

ans = ''

ans += 'R' * (tx - sx)
ans += 'U' * (ty - sy)

ans += 'L' * (tx - sx)
ans += 'D' * (ty - sy)

ans += 'L'
ans += 'U' * (ty - sy + 1)
ans += 'R' * (tx - sx + 1)
ans += 'D'

ans += 'R'
ans += 'D' * (ty - sy + 1)
ans += 'L' * (tx - sx + 1)
ans += 'U'

print(ans)