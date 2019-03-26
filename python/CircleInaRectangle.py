data = input().split()

w = int(data[0])
h = int(data[1])
x = int(data[2])
y = int(data[3])
r = int(data[4])

if y + r > h:
  print("No")
elif y - r < 0:
  print("No")
elif x + r > w:
  print("No")
elif x - r < 0:
  print("No")
else:
  print("Yes")
