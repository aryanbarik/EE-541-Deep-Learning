from func import f
import sys

    #Your script should accept a and b as two numeric command line arguments, i.e., python hw3p1.py
#"1.1" "1.4". Your script must validate that a and b are numeric, verify that a < b, and check
#that f(a)f(b) < 0 — see Bolzano’s Theorem. Write “Range error” to STDERR (standard error)
#if any of these three conditions fail and immediately terminate.

def secant(a,b):
    if not (a < b or f(a)*f(b) < 0 or len(sys.argv) != 2):
        print('Range error', file=sys.stderr)
        
