n = int(input())

data = input().split()

reverse = []

for i in range(n):
  reverse.append(int(data[n-1-i]))

print(*reverse)

