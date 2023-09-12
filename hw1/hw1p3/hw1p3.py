from func import f
import sys

if len(sys.argv)!= 3:
    print('range error', file=sys.stderr)
    sys.exit()

def secant(a,b):
    if (a >= b or f(a)*f(b) >= 0):
        print('range error', file=sys.stderr)
        return
    
    # while not within convergence
    x1 = a
    x2 = b
    x3 = a
    iterations = 0
    
    while ( (abs(x3 - x2) >= 10**-10) or (abs(x2 - x1) >= 10**-10)):
        x3 = x2 - (f(x2) * (x2 - x1)/(f(x2) - f(x1)))
        iterations += 1
        
        if ((abs(x3 - x2) < 10**-10) or (abs(x2 - x1) < 10**-10)):
            break
        
        x1 = x2
        x2 = x3
        
    print(iterations, file=sys.stdout)
    print(x1, file=sys.stdout)
    print(x2, file=sys.stdout)
    print(x3, file=sys.stdout)

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
except ValueError:
    print('range error')

secant(a,b)