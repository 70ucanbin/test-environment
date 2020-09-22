import numpy as np
N, W = map(int, input().rstrip().split(' '))
weight_array = np.zeros(W+1)

for _ in range(N):
  w, v = map(int, input().rstrip().split(' '))
  weight_array[w:] = np.maximum(weight_array[:-w]+v, weight_array[w:])
print(int(weight_array[-1]))
