data = input().split()

a = int(data[0])
b = int(data[1])
c = int(data[2])

if a > b:
  temp = a
  a = b
  b = temp

if b > c:
  temp = b
  b = c
  c = temp

if a > b:
  temp = a
  a = b
  b = temp

if b > c:
  temp = b
  b = c
  c = temp

print("{0} {1} {2}".format(a,b,c))