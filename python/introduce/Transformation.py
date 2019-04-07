string = input()

loop = int(input())

data = []

for i in string:
	data.append(i)

for i in range(loop):
	operate = input().split()

	if operate[0] == "replace":
		a = int(operate[1])
		b = int(operate[2])
		trans = []
		for i in operate[3]:
			trans.append(i)
		ope = 0
		for i in range(a, b+1):
			data[i] = trans[ope]
			ope += 1
	elif operate[0] == "reverse":
		a = int(operate[1])
		b = int(operate[2])
		trans = []
		for i in range(a,b+1):
			trans.append(data[b-i+a])

		ope = 0

		for i in range(a, b+1):
			data[i] = trans[ope]
			ope += 1

	else:	
		a = int(operate[1])
		b = int(operate[2])
		for i in range(a, b+1):
			print(data[i], end = "")
		print()