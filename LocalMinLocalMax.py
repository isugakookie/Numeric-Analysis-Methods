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

my_print = lambda *args: print(*args, end='\n', sep='')

#-----------------------Main----------------------
x = symbols('x')
f = x**3 + 3*x**2 - 24*x
print('f(x)=')
pprint(f)

#first derivative method
printHeader('First Deriviatve')
fd1 = diff(f,x)
print('f\'(x)=')
pprint(fd1)

xsol = solve(fd1, x)
print('\ncritical numbers are ', end='')
pprint2(xsol)

for xval in xsol:
    flag = [False, False]
    left = fd1.subs(x,xval-1)
    right = fd1.subs(x,xval+1)

    if left>0:
        flag[0]=True

    if right>0:
        flag[1]=True

    print('f\'(',xval-1,') = ',left,'\tf\'(',xval+1,') = ', right, sep='')

    if flag[0]==True and flag[1]==False:
        my_print('local max = ',xval)

    elif flag[0]==False and flag[1]==True:
        my_print('local min = ',xval)
    
    print('')

#second derivative method
printHeader('Second Deriviatve')

fd2 = diff(fd1,x)
pprint(fd2)

print('\ncritical numbers are ', end='')
pprint2(xsol)

for xval in xsol:
    flag = False
    sol = fd2.subs(x,xval)

    if sol<0:
        flag=True

    print('f\'(',xval,') = ',sol, sep='')

    if flag==True:
        my_print('local max = ',xval)

    else:
        my_print('local min = ',xval)
    
    print('')