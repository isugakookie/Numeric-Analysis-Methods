from sympy import *
init_printing()

#----------------------Function-------------------
def printHeader(var1):
    print('-'*75)
    print(var1.center(75,' '))
    print('-'*75,end='\n\n')

def pprint2(var1):
    pprint(var1)
    print('')

my_print = lambda *args: print(*args, end='', sep='')

#-----------------------Main----------------------
x, h = symbols('x h')
k = symbols('k', Integer=True)
rf = 4
x0 = 1.8
f = ln(x)
hval = 0.1

printHeader('Variables/Functions')
print('h =',hval,', x0 =',x0)

print('f(x)=')
pprint2(f)

fd = diff(f,x)
print('Derivative =')
pprint(fd)

#---------------------------------------------------------------------------
#                             Central Difference
#---------------------------------------------------------------------------
printHeader('Central Difference')

central = (1/(2*h))*(symbols('f(x+h)')-symbols('f(x-h)'))
pprint(central)

fList = []
fList.append(f.subs(x,x0+hval))
fList.append(f.subs(x,x0-hval))

my_print('f(xk) = ')
pprint(fList)
fList = Array(fList)

centSol = central.subs([(symbols('f(x+h)'),fList[0]),
                        (symbols('f(x-h)'),fList[1]),  
                        (h,hval)])
print('=',round(centSol,rf))

exact = float(fd.subs(x,x0).doit())
print('Exact value =',round(exact,rf))
eError1 = abs(exact-centSol)
my_print('Exact Error is |',round(exact,rf),' - ',round(centSol,rf),'| = ', round(eError1,rf),'\n')

eRel1 = eError1/exact
print('Relative error =')
pprint(Eq(symbols(str(round(eError1,rf)))/symbols(str(round(exact,rf))),symbols(str(round(eRel1,rf)))))

#---------------------------------------------------------------------------
#                             Forward Difference
#---------------------------------------------------------------------------
printHeader('Forward Difference')

forward = (1/h)*(symbols('f(x+h)')-symbols('f(x)'))
pprint(forward)

fList = []
fList.append(f.subs(x,x0+hval))
fList.append(f.subs(x,x0))

my_print('f(xk) = ')
pprint(fList)
fList = Array(fList)

forSol = forward.subs([(symbols('f(x+h)'),fList[0]),
                        (symbols('f(x)'),fList[1]),  
                        (h,hval)])
print('=',round(forSol,rf))

exact = float(fd.subs(x,x0).doit())
print('Exact value =',round(exact,rf))
eError2 = abs(exact-forSol)
my_print('Exact Error is |',round(exact,rf),' - ',round(forSol,rf),'| = ', round(eError2,rf),'\n')

eRel2 = eError2/exact
print('Relative error =')
pprint(Eq(symbols(str(round(eError2,rf)))/symbols(str(round(exact,rf))),symbols(str(round(eRel2,rf)))))

#---------------------------------------------------------------------------
#                            Backward Difference
#---------------------------------------------------------------------------
printHeader('Backward Difference')

backward = (1/h)*(symbols('f(x)')-symbols('f(x-h)'))
pprint(backward)

fList = []
fList.append(f.subs(x,x0))
fList.append(f.subs(x,x0-hval))

my_print('f(xk) = ')
pprint(fList)
fList = Array(fList)

backSol = backward.subs([(symbols('f(x)'),fList[0]),
                        (symbols('f(x-h)'),fList[1]),
                        (h,hval)])
print('=',round(backSol,rf))

exact = float(fd.subs(x,x0).doit())
print('Exact value =',round(exact,rf))
eError3 = abs(exact-backSol)
my_print('Exact Error is |',round(exact,rf),' - ',round(backSol,rf),'| = ', round(eError3,rf),'\n')

eRel3 = eError3/exact
print('Relative error =')
pprint(Eq(symbols(str(round(eError3,rf)))/symbols(str(round(exact,rf))),symbols(str(round(eRel3,rf)))))