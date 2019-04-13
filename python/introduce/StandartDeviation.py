import math

while True:
  n = int(input())

  if n == 0: break

  data = input().split()

  average = 0.0

  for i in data:
    average += int(i)

  average /= n 

  s_th_power = 0.0

  for i in data:
    s_th_power += (int(i)-average) * (int(i)-average)

  s_th_power /= n

  s = 0.0

  s = math.sqrt(s_th_power)

  print("%.8f"%s)