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
    printHeader('Bisection Method')
    x = symbols('x')
    f = 3*exp(x) - 5*x - 4
    rf = 3
    numIteration = 1
    intervals = [0, 2]

    pprint(Eq(symbols('f(x)'),f,evaluate=False))
    """
    while(True):
        sol1 = float(f.subs(x,intervals[0]))
        sol2 = float(f.subs(x,intervals[1]))
        if sol1>0 and sol2<0:
            break
        else:
            intervals = list([intervals[0]+1,intervals[1]+1])
    """
    print('Starting Interval =',intervals)

    
    for i in range (numIteration):
        a = intervals[0]
        b = intervals[1]
        solA = float(f.subs(x,a))
        c = (a + b)/2
        solC = float(f.subs(x,c))
        if (solA>0 and solC<0) or (solA<0 and solC>0):
            intervals = list([a,c])
        elif (solA>0 and solC>0) or (solA<0 and solC<0):
            intervals = list([c,b])
        elif (solC==0):
            print(c,'is the solution')
            break
        print('Interval =',intervals)

__main__()