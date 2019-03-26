m,n = map(int, input().split())

A = [[0 for i in range(n)] for j in range(m)]

for i in range(m):
  data = input().split()
  for j in range(n):
    A[i][j] = int(data[j])

B = [0 for i in range(n)]

for j in range(n):
  data = input()
  B[j] = int(data)

total = [0 for i in range(m)]

for i in range(m):
  for j in range(n):
    total[i] += A[i][j] * B[j]

for i in range(m):
  print(total[i])

