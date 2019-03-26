a,b = map( int, input().split() )

print("{0} {1} {2:.12f}".format( int(a/b), a%b, a/b) )