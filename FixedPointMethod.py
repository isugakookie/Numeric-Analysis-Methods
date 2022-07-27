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
    printHeader('Fixed Point Method')
    x = symbols('x')
    f = 1 + 2/x
    rf = 3
    p0 = 4
    numIteration = 3
    pprint(f)

    xsol = solve(Eq(f,x),x)
    ysol = []
    for i in xsol:
        ysol.append(f.subs(x,i))

    print('roots =', xsol)
    print('f(x) of roots =', ysol)
    p = p0
    for i in range (numIteration):
        p = float(f.subs(x,p))
        print('p',i,' =',round(p,rf), sep='')

__main__()