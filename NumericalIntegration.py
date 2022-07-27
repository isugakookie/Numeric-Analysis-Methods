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
a, b = 0, 1
f = tan(x)

print('f(x)=')
pprint2(f)

fAnti = integrate(f,x)
print('Antiderivative =')
pprint(fAnti)

#---------------------------------------------------------------------------
#                              Trapezoidal Rule
#---------------------------------------------------------------------------
printHeader('Trapezoidal Rule')

trapezoidal = (h/2)*(symbols('f'+str(0))+symbols('f'+str(1)))
pprint(trapezoidal)

hval1 = b - a
print('h =',hval1)

fList = []
xList = []
xval = a
for i in range(2):
    xList.append(xval)
    fList.append(f.subs(x,xval))
    xval+=hval1

my_print('xk = ')
pprint(xList)

my_print('f(xk) = ')
pprint(fList)
fList = Array(fList)

trapSol = trapezoidal.subs([(symbols('f'+str(0)),fList[0]),
                            (symbols('f'+str(1)),fList[1]),  
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
#                                Simpson Rule
#---------------------------------------------------------------------------
printHeader('Simpson Rule')
simpson = (h/3)*(symbols('f'+str(0))+4*symbols('f'+str(1))+symbols('f'+str(2)))
pprint(simpson)

hval2 = (b - a)/2
print('h =',hval2)

fList = []
xList = []
xval = a
for i in range(3):
    xList.append(xval)
    fList.append(f.subs(x,xval))
    xval+=hval2

my_print('xk = ')
pprint(xList)

my_print('f(xk) = ')
pprint(fList)
fList = Array(fList)

simpSol = simpson.subs([(symbols('f'+str(0)),fList[0]),
                        (symbols('f'+str(1)),fList[1]),
                        (symbols('f'+str(2)),fList[2]),
                        (h,hval2)])
print('=',round(simpSol,rf))

print('Exact value =',exact)
eError2 = abs(exact-simpSol)
my_print('Exact Error is |',exact,' - ',round(simpSol,rf),'| = ', round(eError2,rf),'\n')

eRel2 = eError2/exact
print('Relative error =')
pprint(Eq(symbols(str(round(eError2,rf)))/symbols(str(exact)),symbols(str(round(eRel2,rf)))))

#---------------------------------------------------------------------------
#                                Simpson's 3/8 Rule
#---------------------------------------------------------------------------
printHeader('Simpson\'s 3/8 Rule')
simpson38 = ((3*h)/8)*(symbols('f'+str(0))+3*symbols('f'+str(1))+3*symbols('f'+str(2))+symbols('f'+str(3)))
pprint(simpson38)

hval3 = (b - a)/3
print('h =',hval3)

fList = []
xList = []
xval = a
for i in range(4):
    xList.append(xval)
    fList.append(f.subs(x,xval))
    xval+=hval3

my_print('xk = ')
pprint(xList)

my_print('f(xk) = ')
pprint(fList)
fList = Array(fList)

simp38Sol = simpson38.subs([(symbols('f'+str(0)),fList[0]),
                        (symbols('f'+str(1)),fList[1]),
                        (symbols('f'+str(2)),fList[2]),
                        (symbols('f'+str(3)),fList[3]),
                        (h,hval3)])
print('=',round(simp38Sol,rf))

print('Exact value =',exact)
eError3 = abs(exact-simp38Sol)
my_print('Exact Error is |',exact,' - ',round(simp38Sol,rf),'| = ', round(eError3,rf),'\n')

eRel3 = eError3/exact
print('Relative error =')
pprint(Eq(symbols(str(round(eError3,rf)))/symbols(str(exact)),symbols(str(round(eRel3,rf)))))