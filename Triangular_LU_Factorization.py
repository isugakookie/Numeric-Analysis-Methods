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

# When the Gaussian elimination is performed without any row interchanges. 
# So, no pivoting and akk ≠ 0 for all k = 0, 1, 2, …, N.
def case1(A, B):
    printHeader("Case 1")
    L = Matrix([[1, 0, 0], [symbols('m21'), 1, 0], [symbols('m31'), symbols('m32'), 1]])
    U = Matrix(A)

    #gaussian elimination
    m21 = U[1,0]/U[0,0]
    print('m21 =', m21)

    m31 = U[2,0]/U[0,0]
    print('m31 =', m31)

    temprow = U[1,:]
    U.row_del(1)
    U = U.row_insert(1, temprow - m21*U[0,:])

    temprow = U[2,:]
    U.row_del(2)
    U = U.row_insert(2, temprow - m31*U[0,:])

    #m32 = U[2,1]/U[1,1]
    m32=0
    print('m32 =', m32)

    temprow = U[2,:]
    U.row_del(2)
    U = U.row_insert(2, temprow - m32*U[1,:])

    L = L.subs([(symbols('m21'), m21),
                (symbols('m31'), m31),
                (symbols('m32'), m32)])

    pprint(Eq(symbols('A'), A, evaluate=False))
    pprint(Eq(symbols('L'), L, evaluate=False))
    pprint(Eq(symbols('U'), U, evaluate=False))
    pprint(Eq(symbols('B'), B, evaluate=False))

    Y = Matrix([symbols('y1'), symbols('y2'), symbols('y3')])
    pprint(Eq(L*Y, B))
    ySol = solve(Eq(L*Y, B),(symbols('y1'), symbols('y2'), symbols('y3')))
    pprint(ySol)
    
    Y = Y.subs([(symbols('y1'),ySol[symbols('y1')]),
                (symbols('y2'),ySol[symbols('y2')]),
                (symbols('y3'),ySol[symbols('y3')])])
    
    pprint(Eq(symbols('Y'), Y, evaluate=False))

    X = Matrix([symbols('x1'), symbols('x2'), symbols('x3')])
    pprint(Eq(U*X, Y))
    xSol = solve(Eq(U*X, Y),(symbols('x1'), symbols('x2'), symbols('x3')))
    pprint(xSol)
    
    X = X.subs([(symbols('x1'),xSol[symbols('x1')]),
                (symbols('x2'),xSol[symbols('x2')]),
                (symbols('x3'),xSol[symbols('x3')])])
    
    pprint(Eq(symbols('X'), X, evaluate=False))

# When the Gaussian elimination is performed with row interchange that is, 
# partial pivoting or any of akk = 0.
def case2(A, B):
    printHeader("Case 2")
    L = Matrix([[1, 0, 0], [symbols('m21'), 1, 0], [symbols('m31'), symbols('m32'), 1]])
    U = Matrix(A)
    P=eye(A.rows)

    pprint(Eq(symbols('A'), A, evaluate=False))

    #switch rows
    temprow = U[1,:]
    U.row_del(1)
    U = U.row_insert(0, temprow)
    
    temprow = P[1,:]
    P.row_del(1)
    P = P.row_insert(0, temprow)
    
    #gaussian elimination
    m21 = U[1,0]/U[0,0]
    print('m21 =', m21)

    m31 = U[2,0]/U[0,0]
    print('m31 =', m31)

    temprow = U[1,:]
    U.row_del(1)
    U = U.row_insert(1, temprow - m21*U[0,:])

    temprow = U[2,:]
    U.row_del(2)
    U = U.row_insert(2, temprow - m31*U[0,:])

    #switch rows
    temprow = U[1,:]
    U.row_del(1)
    U = U.row_insert(2, temprow)

    temprow = P[1,:]
    P.row_del(1)
    P = P.row_insert(2, temprow)

    #gaussian elimination
    m32 = U[2,1]/U[1,1]
    print('m32 =', m32)

    temprow = U[2,:]
    U.row_del(2)
    U = U.row_insert(2, temprow - m32*U[1,:])

    L = L.subs([(symbols('m21'), m21),
                (symbols('m31'), m31),
                (symbols('m32'), m32)])
    
    pprint(Eq(symbols('L'), L, evaluate=False))
    pprint(Eq(symbols('U'), U, evaluate=False))
    pprint(Eq(symbols('B'), B, evaluate=False))
    pprint(Eq(symbols('P'), P, evaluate=False))

    Y = Matrix([symbols('y1'), symbols('y2'), symbols('y3')])
    pprint(Eq(L*Y, P*B))
    ySol = solve(Eq(L*Y, P*B),(symbols('y1'), symbols('y2'), symbols('y3')))
    pprint(ySol)
    
    Y = Y.subs([(symbols('y1'),ySol[symbols('y1')]),
                (symbols('y2'),ySol[symbols('y2')]),
                (symbols('y3'),ySol[symbols('y3')])])
    
    pprint(Eq(symbols('Y'), Y, evaluate=False))

    X = Matrix([symbols('x1'), symbols('x2'), symbols('x3')])
    pprint(Eq(U*X, Y))
    xSol = solve(Eq(U*X, Y),(symbols('x1'), symbols('x2'), symbols('x3')))
    pprint(xSol)
    
    X = X.subs([(symbols('x1'),xSol[symbols('x1')]),
                (symbols('x2'),xSol[symbols('x2')]),
                (symbols('x3'),xSol[symbols('x3')])])
    
    pprint(Eq(symbols('X'), X, evaluate=False))

#---------------------------------------------------------------------------
#                                    Main
#---------------------------------------------------------------------------

def __main__():
    printHeader("System of Equations")

    A = Matrix([[1, 2, -2], [2, 4, -9], [3, 1, 2]])
    B = Matrix([-1,3,-1])
    case1(A, B)
    case2(A, B)

    L, U, _ = A.LUdecomposition()
    pprint(Eq(symbols('L'), L, evaluate=False))
    pprint(Eq(symbols('U'), U, evaluate=False))

__main__()