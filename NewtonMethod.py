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
    printHeader('Newton Method')
    x = symbols('x')
    f = 3*exp(x) - 5*x - 4
    fd = diff(f,x)
    rf = 3
    p0 = 0
    numIteration = 1
    
    pprint(Eq(symbols('f(x)'),f,evaluate=False))
    pprint(Eq(symbols('f\'(x)'),fd,evaluate=False))

    p1 = p0
    errorList = []
    for i in range (numIteration):
        p0 = p1
        p1 = p0-(float(f.subs(x,p0))/float(fd.subs(x,p0)))
        print(float(f.subs(x,p0)), float(fd.subs(x,p0)))
        errorList.append(abs(p1-p0))
        print('p',i,' =',round(p1,rf), sep='')
    
    for i in range(len(errorList)):
        if i!=0:
            print('error =',round(errorList[i]/errorList[i-1],rf))

__main__()