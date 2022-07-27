from sympy import *
init_printing()

#---------------------------------------------------------------------------
#                                  Functions
#---------------------------------------------------------------------------
def printHeader(var1):
    print('-'*75)
    print(var1.center(75,' '))
    print('-'*75,end='\n\n')

def pprint2(var1):
    pprint(var1)
    print('')

my_print = lambda *args: print(*args, end='', sep='')

#---------------------------------------------------------------------------
#                                    Main
#---------------------------------------------------------------------------

def __main__():
    printHeader('Secant Method')
    x = symbols('x')
    f = x**2 + 23 - 10*x
    rf = 3
    numIteration = 3
    intervals = [3, 4]

    pprint(Eq(symbols('f(x)'),f,evaluate=False))

    print('Starting Interval =',intervals)

    
    for i in range (numIteration):
        p0 = intervals[0]
        p1 = intervals[1]
        solP0 = float(f.subs(x,p0))
        solP1 = float(f.subs(x,p1))
        p = p1 - (solP1*(p1-p0)/(solP1 - solP0))
        intervals = list([p1,p])
        print('Interval = [',round(intervals[0],rf), ',', round(intervals[1],rf), ']', sep='')

__main__()