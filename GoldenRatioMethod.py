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
r = 0.61803
intervalTemp = [0.5,2.5]
numIteration = 2
f = (x**2)/2 - 4*x - x*cos(x)
rf = 4

print('f(x)=')
pprint2(f)
printHeader('Intervals')
for i in range(numIteration):
    a = intervalTemp[0]
    b = intervalTemp[1]
    my_print('Let a',i,' = ',a,' & b',i,' = ',b,'\n')

    c = float(a) + (1-r)*float(b - a)
    my_print('c = a',i,' + (1 - r)(b',i,' - a',i,')')
    my_print('= ',a,' + (1 - ',r,')(',b,' - ',a,')')
    print("=",c,'\n')

    d = float(b) - (1-r)*float(b - a)
    my_print('d = b',i,' - (1 - r)(b',i,' - a',i,')')
    my_print('= ',b,' - (1 - ',r,')(',b,' - ',a,')')
    print("=",d)

    fc = f.subs(x, c)
    fd = f.subs(x, d)
    if fc<=fd:
        intervalTemp=[a,d]
        my_print('f(c)<=f(d), New Interval is [',round(intervalTemp[0],rf),', ',round(intervalTemp[1],rf),']')
    else:
        intervalTemp=[c,b]
        my_print('f(c)>f(d), New Interval is [',round(intervalTemp[0],rf),', ',round(intervalTemp[1],rf),']')
    print('')