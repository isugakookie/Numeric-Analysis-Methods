from sympy import *
init_printing()

#---------------------------------------------------------------------------
#                              Global Variables
#---------------------------------------------------------------------------
x, y, j, k = symbols('x y j k')
xList = [0,1,2]
f = x**4 - 2*x
rf = 4
N = 2
yList = []
for xval in xList:
    yList.append(f.subs(x,xval))

xList = Array(xList)
yList = Array(yList)

def __main__():
    p = summation(IndexedBase('y')[k]*IndexedBase('L')[N,k],(k,0,N))
    print(p)
    
    L = product((x-IndexedBase('x')[j])/(IndexedBase('x')[k]-IndexedBase('x')[j]),(j,0,N))
    pprint(L)
    p1 = p
    for i in range(N+1):
        L1 = L.subs([(x-IndexedBase('x')[i],1),
                    (IndexedBase('x')[k]-IndexedBase('x')[i],1),
                    (k,i)])

        p1 = p1.subs(IndexedBase('L')[N,i],L1)
        pprint(p1)

    p1 = p1.subs([(IndexedBase('x'),xList),
                  (IndexedBase('y'),yList)])

    print('\nLangrange Polynomial = ')
    pprint(p1.expand(mul=True))

__main__()