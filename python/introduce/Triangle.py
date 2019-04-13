import math

a,b,degree = map(float, input().split())

rad = degree * math.pi / 180.0

Square = a * b / 2 * math.sin(rad)

c = b / math.sin(rad)

L =  a + b + math.sqrt(a*a + b*b - 2.0*a*b*math.cos(rad) )

h = b * math.sin(rad)

print("%.6f"%Square)
print("%.6f"%L)
print("%.6f"%h)