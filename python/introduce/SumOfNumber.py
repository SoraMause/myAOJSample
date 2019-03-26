import math

while True:
  data = input()
  total = 0
  if int(data) == 0:
    break

  for i in data:
    total += int(i)
  
  print(total)