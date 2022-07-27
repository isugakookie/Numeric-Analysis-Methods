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
    printHeader('Regula Falsi Method')
    x = symbols('x')
    f = x**2 + 2*x - 4 - 2*x
    rf = 3
    numIteration = 2
    intervals = [0, 3]

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
        solB = float(f.subs(x,b))
        c = b - ((solB*(b - a))/(solB-solA))
        solC = float(f.subs(x,c))
        print(solA, solB, solC)
        if (solA>0 and solC<0) or (solA<0 and solC>0):
            intervals = list([a,c])
        elif (solA>0 and solC>0) or (solA<0 and solC<0):
            intervals = list([c,b])
        elif (solC==0):
            print(c,'is the solution')
            break
        print('Interval = [',round(intervals[0],rf), ',', round(intervals[1],rf), ']', sep='')

__main__()