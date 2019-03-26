data = input()
output = []
for i in data:
  if i.islower():
    output.append(i.upper())
  else:
    output.append(i.lower())

for i in output:
  print(i, end="")

print()