while True:
    data = input().split()
    a = int(data[0])
    b = int(data[1])
    if a == 0 and b == 0:
        break
    if a < b:
        print(a, b)
    else:
        print(b, a)