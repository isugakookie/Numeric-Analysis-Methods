from sympy import *
init_printing()

#---------------------------------------------------------------------------
#                              Global Variables
#---------------------------------------------------------------------------
x = symbols('x')
rf = 3
f = x**4
dataList = dict([(2,0.92), (2.06,0.81), (2.12,0.73)])

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
#                             Central Difference
#---------------------------------------------------------------------------
def centralNoData(h, x0, exact):
    printHeader('Central Difference')

    central = (1/(symbols('h')**2))*(symbols('f(x+h)')+symbols('f(x-h)')-2*symbols('f(x)'))
    print('f\'\'(x) = ')
    pprint(central)

    fList = []
    fList.append(f.subs(x,x0+h))
    fList.append(f.subs(x,x0-h))
    fList.append(f.subs(x,x0))

    my_print('f(xk) = ')
    pprint(fList)
    fList = Array(fList)

    centSol = central.subs([(symbols('f(x+h)'),fList[0]),
                            (symbols('f(x-h)'),fList[1]),
                            (symbols('f(x)'),fList[2]),
                            (symbols('h'),h)])
    print('=',round(centSol,rf))

    print('Exact value =',round(exact,rf))
    eError1 = abs(exact-centSol)
    my_print('Exact Error is |',round(exact,rf),' - ',round(centSol,rf),'| = ', round(eError1,rf),'\n')

    eRel1 = eError1/exact
    print('Relative error =')
    pprint(Eq(symbols(str(round(eError1,rf)))/symbols(str(round(exact,rf))),symbols(str(round(eRel1,rf)))))

def centralWithData(h, x0):
    printHeader('Central Difference with Data')
    print('x = ',x0)
    
    central = (1/(symbols('h')**2))*(symbols('f(x+h)')+symbols('f(x-h)')-2*symbols('f(x)'))
    print('f\'\'(x) = ')
    pprint(central)

    fList = []
    fList.append(dataList[x0+h])
    fList.append(dataList[x0-h])
    fList.append(dataList[x0])

    my_print('f(xk) = ')
    pprint(fList)
    fList = Array(fList)

    centSol = central.subs([(symbols('f(x+h)'),fList[0]),
                            (symbols('f(x-h)'),fList[1]),
                            (symbols('f(x)'),fList[2]),
                            (symbols('h'),h)])
    print('=',round(centSol,rf))

#---------------------------------------------------------------------------
#                             Forward Difference
#---------------------------------------------------------------------------
def forwardNoData(h, x0, exact):
    printHeader('Forward Difference')

    forward = (1/(2*symbols('h')))*((-3)*symbols('f(x)')+4*symbols('f(x+h)')-symbols('f(x+2h)'))
    print('f\'(x) = ')
    pprint(forward)

    fList = []
    fList.append(f.subs(x,x0))
    fList.append(f.subs(x,x0+h))
    fList.append(f.subs(x,x0+(2*h)))

    my_print('f(xk) = ')
    pprint(fList)
    fList = Array(fList)

    forSol = forward.subs([ (symbols('f(x)'),fList[0]),
                            (symbols('f(x+h)'),fList[1]),
                            (symbols('f(x+2h)'),fList[2]),
                            (symbols('h'),h)])
    print('=',round(forSol,rf))

    print('Exact value =',round(exact,rf))
    eError2 = abs(exact-forSol)
    my_print('Exact Error is |',round(exact,rf),' - ',round(forSol,rf),'| = ', round(eError2,rf),'\n')

    eRel2 = eError2/exact
    print('Relative error =')
    pprint(Eq(symbols(str(round(eError2,rf)))/symbols(str(round(exact,rf))),symbols(str(round(eRel2,rf)))))

def forwardWithData(h, x0):
    printHeader('Forward Difference with Data')
    print('x = ',x0)

    forward = (1/(2*symbols('h')))*((-3)*symbols('f(x)')+4*symbols('f(x+h)')-symbols('f(x+2h)'))
    print('f\'(x) = ')
    pprint(forward)

    fList = []
    fList.append(dataList[x0])
    fList.append(dataList[x0+h])
    fList.append(dataList[x0+(2*h)])

    my_print('f(xk) = ')
    pprint(fList)
    fList = Array(fList)

    forSol = forward.subs([ (symbols('f(x)'),fList[0]),
                            (symbols('f(x+h)'),fList[1]),
                            (symbols('f(x+2h)'),fList[2]),
                            (symbols('h'),h)])
    print('=',round(forSol,rf))

#---------------------------------------------------------------------------
#                            Backward Difference
#---------------------------------------------------------------------------
def backwardNoData(h, x0, exact):
    printHeader('Backward Difference')

    backward = (1/(2*symbols('h')))*(3*symbols('f(x)')-4*symbols('f(x-h)')+symbols('f(x-2h)'))
    print('f\'(x) = ')
    pprint(backward)

    fList = []
    fList.append(f.subs(x,x0))
    fList.append(f.subs(x,x0-h))
    fList.append(f.subs(x,x0-(2*h)))

    my_print('f(xk) = ')
    pprint(fList)
    fList = Array(fList)

    backSol = backward.subs([(symbols('f(x)'),fList[0]),
                            (symbols('f(x-h)'),fList[1]),
                            (symbols('f(x-2h)'),fList[2]),
                            (symbols('h'),h)])
    print('=',round(backSol,rf))

    print('Exact value =',round(exact,rf))
    eError3 = abs(exact-backSol)
    my_print('Exact Error is |',round(exact,rf),' - ',round(backSol,rf),'| = ', round(eError3,rf),'\n')

    eRel3 = eError3/exact
    print('Relative error =')
    pprint(Eq(symbols(str(round(eError3,rf)))/symbols(str(round(exact,rf))),symbols(str(round(eRel3,rf)))))

def backwardWithData(h, x0):
    printHeader('Backward Difference with Data')
    print('x = ',x0)

    backward = (1/(2*symbols('h')))*(3*symbols('f(x)')-4*symbols('f(x-h)')+symbols('f(x-2h)'))
    print('f\'(x) = ')
    pprint(backward)

    fList = []
    fList.append(dataList[x0])
    fList.append(dataList[x0-h])
    fList.append(dataList[x0-(2*h)])

    my_print('f(xk) = ')
    pprint(fList)
    fList = Array(fList)

    backSol = backward.subs([(symbols('f(x)'),fList[0]),
                            (symbols('f(x-h)'),fList[1]),
                            (symbols('f(x-2h)'),fList[2]),
                            (symbols('h'),h)])
    print('=',round(backSol,rf))

#---------------------------------------------------------------------------
#                                    Main
#---------------------------------------------------------------------------

def __main__():
    hval = 0.1
    x0 = 1

    printHeader('Variables/Functions')
    print('h =',hval,', x0 =',x0)

    print('f(x)=')
    pprint2(f)

    fd = diff(f,x)
    print('Derivative =')
    pprint(fd)
    fd2 = diff(fd,x)
    print('Derivative =')
    pprint(fd2)

    exact1 = float(fd2.subs(x,x0).doit())
    exact2 = float(fd2.subs(x,x0).doit())

    centralNoData(hval, x0, exact1)
    #forwardNoData(hval, x0, exact2)
    #backwardNoData(hval, x0, exact2)

    xList=[2, 2.06]
    hval = 2.06-2
    print(hval)
    x1 = 1.5

    #centralWithData(hval, x1)
    forwardWithData(hval, 2)
    centralWithData(hval, 2.06)
    """
    for i, val in enumerate(xList):
        if i==0:
            forwardWithData(hval, val)
        elif i==len(xList)-1:
            backwardWithData(hval, val)
    """
__main__()