from func import f
import sys

if len(sys.argv)!= 3:
    print('range error', file=sys.stderr)
    sys.exit()

def secant(a,b):
    if not (a < b or f(a)*f(b) < 0):
        print('range error', file=sys.stderr)
        return
    
    # while not within convergence
    x2 = b
    x1 = a
    x3 = 0
    iterations = 0
    
    while ( abs(x3 - x2) > 10**-10 or abs(x2 - x1) > 10**-10 ):
        x3 = x2 - (f(x2) * (x2 - x1)/(f(x2) - f(x1)))
        iterations += 1
        
        x1 = x2
        x2 = x3
        
    print(iterations, file=sys.stdout)
    print(x1, file=sys.stdout)
    print(x2, file=sys.stdout)
    print(x3, file=sys.stdout)
    
a = float(sys.argv[1])
b = float(sys.argv[2])

secant(a,b)