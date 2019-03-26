suits = ['S','H','C','D']

table = [[False]*14 for i in range(4)]

n = int(input())

for loop in range(n):
  mark,num = input().split()

  num = int(num)

  if mark == 'S':
    table[0][num] = True
  elif mark == 'H':
    table[1][num] = True
  elif mark == 'C':
    table[2][num] = True
  else:
    table[3][num] = True

for i in range(4):
  for j in range(1,14):
    if table[i][j] == False:
      print(suits[i], j)