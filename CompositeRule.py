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
M = 4
M1 = 3
a, b = 0, 1
f = tan(x)

print('f(x)=')
pprint2(f)

fAnti = integrate(f,x)
print('Antiderivative =')
pprint(fAnti)

#---------------------------------------------------------------------------
#                         Composite Trapezoidal Rule
#---------------------------------------------------------------------------

printHeader('Composite Trapezoidal Rule')

trapezoidal = (h/2)*(symbols('f'+str(0))+2*Sum(IndexedBase('f')[k],(k,1,M-1))+symbols('f'+str(M)))
pprint(trapezoidal)

hval1 = (b - a)/M
print('h =',hval1)

fList = []
xList = []
xval = a
for i in range(M+1):
    xList.append(xval)
    fList.append(f.subs(x,xval))
    xval+=hval1

my_print('xk = ')
pprint(xList)

my_print('f(xk) = ')
pprint(fList)
fList = Array(fList)

trapSol = trapezoidal.subs([(symbols('f'+str(0)),fList[0]),
                            (symbols('f'+str(M)),fList[M]),
                            (Sum(IndexedBase('f')[k],(k,1,M-1)),summation(fList[k],(k,1,M-1))),
                            (h,hval1)])
print('=',round(trapSol,rf))

exact = float(Integral(f.subs(x,k),(k,a,b)).doit())
print('Exact value =',exact)
eError1 = abs(exact-trapSol)
my_print('Exact Error is |',exact,' - ',round(trapSol,rf),'| = ', round(eError1,rf),'\n')

eRel1 = eError1/exact
print('Relative error =')
pprint(Eq(symbols(str(round(eError1,rf)))/symbols(str(exact)),symbols(str(round(eRel1,rf)))))

#---------------------------------------------------------------------------
#                           Composite Simpson Rule
#---------------------------------------------------------------------------
printHeader('Composite Simpson Rule')
simpson = (h/3)*(symbols('f'+str(0))+4*Sum(IndexedBase('f')[2*k-1],(k,1,M1))+2*Sum(IndexedBase('f')[2*k],(k,1,M1-1))+symbols('f'+str(2*M1)))
pprint(simpson)

hval2 = (b - a)/(2*M1)
print('h =',hval2)

fList = []
xList = []
xval = a
for i in range(2*(M1)+1):
    xList.append(xval)
    fList.append(f.subs(x,xval))
    xval+=hval2

my_print('xk = ')
pprint(xList)

my_print('f(xk) = ')
pprint(fList)
fList = Array(fList)

simpSol = simpson.subs([(symbols('f'+str(0)),fList[0]),
                        (symbols('f'+str(2*M1)),fList[2*M1]), 
                        (Sum(IndexedBase('f')[2*k-1],(k,1,M1)),summation(fList[2*k-1],(k,1,M1))), 
                        (Sum(IndexedBase('f')[2*k],(k,1,M1-1)),summation(fList[2*k],(k,1,M1-1))), 
                        (h,hval2)])
print('=',round(simpSol,rf))

print('Exact value =',exact)
eError2 = abs(exact-simpSol)
my_print('Exact Error is |',exact,' - ',round(simpSol,rf),'| = ', round(eError2,rf),'\n')

eRel2 = eError2/exact
print('Relative error =')
pprint(Eq(symbols(str(round(eError2,rf)))/symbols(str(exact)),symbols(str(round(eRel2,rf)))))