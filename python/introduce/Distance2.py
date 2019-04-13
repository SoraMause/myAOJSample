import math

n = int(input())

x = input().split()

y = input().split()

Manhattan = 0.0

Euclidean = 0.0

Chebyshev = 0.0

Minkowski = 0.0

for i in range(n):
  Manhattan += abs(int(x[i])- int(y[i]))

  Euclidean += math.pow((int(x[i])- int(y[i])), 2.0)

  Chebyshev += math.pow(abs(int(x[i])- int(y[i])), 3.0)

  if Minkowski < abs((int(x[i])- int(y[i]))): Minkowski = abs(int(x[i])-int(y[i])) 

Euclidean = math.sqrt(Euclidean)
Chebyshev = Chebyshev**(1/3)
  
print("%.8f"%Manhattan)
print("%.8f"%Euclidean)
print("%.8f"%Chebyshev)
print("%.8f"%Minkowski)