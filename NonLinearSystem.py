from sympy import *
init_printing()

#---------------------------------------------------------------------------
#                              Global Variables
#---------------------------------------------------------------------------
x, y = symbols('x y')
numIteration = 2
rf = 3
Intervals = [0,0]

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

def Jacobi(expr1, expr2, list1):
    printHeader('Jacobi Method')

    eq1 = solve(expr1,x)
    eq2 = solve(expr2,y)
    pprint(eq1)
    pprint(eq2)

    for i in range(numIteration):
        xval = float(eq1[0].subs(y,list1[1]))
        yval = float(eq2[1].subs(x,list1[0]))
        print('New Interval = (',round(xval,rf),',',round(yval,rf),')',sep='')
        list1 = list([xval, yval])

def gaussSeidel(expr1, expr2, list1):
    printHeader('Gauss-Seidel Method')

    eq1 = solve(expr1,x)
    eq2 = solve(expr2,y)
    pprint(eq1)
    pprint(eq2)

    for i in range(numIteration):
        xval = float(eq1[0].subs(y,list1[1]))
        yval = float(eq2[1].subs(x,xval))
        print('New Interval = (',round(xval,rf),',',round(yval,rf),')',sep='')
        list1 = list([xval, yval])

#---------------------------------------------------------------------------
#                                    Main
#---------------------------------------------------------------------------

def __main__():
    printHeader("System of Equations")
    expr1 = Eq(2*x + y, 1)
    expr2 = Eq(x**2 + y**2, 4)
    pprint(expr1)
    pprint(expr2)
    Jacobi(expr1, expr2, Intervals)
    gaussSeidel(expr1, expr2, Intervals)

__main__()