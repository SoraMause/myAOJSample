table = [0 for i in range(27)]
 
letters = "abcdefghijklmnopqrstuvwxyz"
input_str = input()
 
for A in input_str:
  index = 0
  for B in letters:
    if A == B or A == B.upper():
      table[index] += 1
      break
    index += 1
 
for i in range(len(letters)):
  print("%s : %d"%(letters[i],table[i]))