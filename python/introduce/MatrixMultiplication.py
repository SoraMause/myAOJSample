n,m,l = map(int, input().split())

A = [[0 for i in range(m)] for j in range(n) ]

B = [[0 for i in range(l)] for j in range(m) ]

C = [[0 for i in range(l)] for j in range(n) ]

for i in range(n):
  data = input().split()
  for j in range(m):
    A[i][j] = int(data[j])
    
for i in range(m):
  data = input().split()
  for j in range(l):
    B[i][j] = int(data[j])

for i in range(n):
  for j in range(l):
    for k in range(m):
      C[i][j] += A[i][k] * B[k][j]

for i in range(n):
  print(*C[i])