from sympy import *
init_printing()

#----------------------Function-------------------
def findDom(list1):
    maxVal = 0
    for val in list1:
        if abs(val)>abs(maxVal):
            maxVal = val
    return maxVal

def pprint2(var1):
    pprint(var1)
    print('')

my_print = lambda *args: print(*args, end='\n\n', sep='')

#-----------------------Main----------------------
A = Matrix([[1, 3, -1], [0, 5, 6], [0, 1, 2]])
x0 = Matrix([0, -2, 1])
numIteration = 1

l = symbols('λ')
I = eye(3)
Il = I*l
eA = A-Il
pprint2(A)
pprint2(eA)

#expansion
r1c1 = eA.row(0).col(0)[0]
r2c1 = eA.row(1).col(0)[0]
r3c1 = eA.row(2).col(0)[0]
pprint(r1c1)
pprint(r2c1)
pprint(r3c1)
eA1 = eA[1:3,1:3]
pprint2(eA1)
eA2 = eA[0,1:3]
eA2 = eA2.row_insert(1,eA[2,1:3])
pprint2(eA2)
eA3 = eA[0:2,1:3]
pprint2(eA3)

edA1 = eA1.det()
edA2 = eA2.det()
edA3 = eA3.det()

#printing out the expanded equations
print(r1c1*(eA1[0,0]*eA1[1,1]-eA1[0,1]*eA1[1,0]))
print(r2c1*(eA2[0,0]*eA2[1,1]-eA2[0,1]*eA2[1,0]))
print(r3c1*(eA3[0,0]*eA3[1,1]-eA3[0,1]*eA3[1,0]))

eVals = r1c1*edA1 - r2c1*edA2 + r3c1*edA3
pprint2(eVals)
eVals = solve(eVals,l)
print('eigenvalues = ', end='')
pprint2(eVals)

domEval = findDom(eVals)
my_print('Dominant eigenvalue: ',domEval)

eVals2 = A.eigenvals()
pprint2(eVals2)
eVects = A.eigenvects()
print('eigenvectors = ')
pprint2(eVects)

x = x0
for i in range(numIteration):
    y = A*x
    pprint(Eq(symbols('y'+str(i)),y,evaluate=False))
    c = findDom(y)
    print('c',i,' = ',c,sep='')
    x = (1/c)*y
    pprint2(Eq(symbols('x'+str(i)),x,evaluate=False))