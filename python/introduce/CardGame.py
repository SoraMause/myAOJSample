N = int(input())
taro_point=0
hanako_point=0
for i in range(N):
  taro,hanako=input().split()
  if taro < hanako:
    hanako_point+=3
  elif taro == hanako:
    taro_point +=1
    hanako_point +=1
  else:
    taro_point +=3

print(taro_point,hanako_point)