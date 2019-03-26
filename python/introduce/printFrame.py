while True:
  a,b = map(int,input().split())

  if a == 0 & b == 0:
    break

  for i in range(a):
    if i == 0:
      print("#"*b)
    elif i == a-1:
      print("#"*b)
      print()
    else:
      print("#"+"."*(b-2)+"#")