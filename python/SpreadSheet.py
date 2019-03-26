n,m = map(int, input().split())

A = [[0 for i in range(m+1)] for j in range(n+1)]

for i in range(n):
  data = input().split()

  for j in range(m):
    A[i][j] = int(data[j])

for i in range(n):
  for j in range(m):
    A[i][m] += A[i][j]

for j in range(m+1):
  for i in range(n):
    A[n][j] += A[i][j]

for i in range(n+1):
    print(*A[i])