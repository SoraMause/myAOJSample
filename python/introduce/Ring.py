s = input()
p = input()

check = False

for i in range(len(s)):
  is_ans = True
  for k in range(len(p)):
    if s[(i+k)%(len(s))] != p[k]:
      is_ans = False
      break

  if is_ans:
    check = True
    break

if check:
  print("Yes")
else:
  print("No")

    