from sympy import *
init_printing()

#---------------------------------------------------------------------------
#                              Global Variables
#---------------------------------------------------------------------------
x, y, z = symbols('x y z')
numIteration = 2
rf = 3
Intervals = [0,0,0]

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

def Jacobi(expr1, expr2, expr3, list1):
    printHeader('Jacobi Method')

    eq1 = solve(expr1,x)
    eq2 = solve(expr2,y)
    eq3 = solve(expr3,z)
    pprint(eq1)
    pprint(eq2)
    pprint(eq3)

    for i in range(numIteration):
        xval = float(eq1[0].subs([(y, list1[1]),
                                  (z, list1[2])]))
        yval = float(eq2[0].subs([(x, list1[0]),
                                  (z, list1[2])]))
        zval = float(eq3[0].subs([(x, list1[0]),
                                  (y, list1[1])]))
        print('New Interval = (',round(xval,rf),',',round(yval,rf),',',round(zval,rf),')',sep='')
        list1 = list([xval, yval, zval])

def gaussSeidel(expr1, expr2, expr3, list1):
    printHeader('Gauss-Seidel Method')

    eq1 = solve(expr1,x)
    eq2 = solve(expr2,y)
    eq3 = solve(expr3,z)
    pprint(eq1)
    pprint(eq2)
    pprint(eq3)

    for i in range(numIteration):
        xval = float(eq1[0].subs([(y, list1[1]),
                                  (z, list1[2])]))
        yval = float(eq2[0].subs([(x, xval),
                                  (z, list1[2])]))
        zval = float(eq3[0].subs([(x, xval),
                                  (y, yval)]))
        print('New Interval = (',round(xval,rf),',',round(yval,rf),',',round(zval,rf),')',sep='')
        list1 = list([xval, yval, zval])

#---------------------------------------------------------------------------
#                                    Main
#---------------------------------------------------------------------------

def __main__():
    printHeader("System of Equations")
    expr1 = Eq(x + z, 2)
    expr2 = Eq(-x + y, 0)
    expr3 = Eq(x + 2*y - 3*z, 0)
    pprint(expr1)
    pprint(expr2)
    pprint(expr3)
    Jacobi(expr1, expr2, expr3, Intervals)
    gaussSeidel(expr1, expr2, expr3, Intervals)

__main__()