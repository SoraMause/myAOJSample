word = input().upper()

ans = 0
data = []

while True:
  text = input()

  if text == "END_OF_TEXT":
    break

  data = text.upper().split()

  for i in data:
    if word == i:
      ans += 1


print(ans)