import itertools
from sympy import *

#----------------------Function-------------------
def stringToIntList(List1):
    List2 = []
    for ch in List1:
        List2.append(int(ch))
    return List2
    
def printList(list1):
    for row in list1:
        print(row)
    print('')

def sumList(list1):
    sumVal = 0
    for val in list1:
        sumVal+=val
    return sumVal

def printTable(list1):
    f = open("output1.csv", "w")
    f.write(",,For Normal Equation,,For Root Square Mean Error,,"+"\n")
    f.write("x_k,y_k,x_k^2,x_ky_k,f(x_k),f(x_k)-y_k,(f(x_k)-y_k)^2"+"\n")
    
    for i in range(len(list1[0])):
        str1 = ""
        for j in range(len(list1)):
            if j!=len(list1)-1:
                str1 = str1+str(list1[j][i])+","
            else:
                str1 = str1+str(list1[j][i])
        if i!=len(list1[0])-1:
            f.write(str1+"\n")
        else:
            f.write(str1)
    
    f.close()

#-----------------------Main----------------------
roundF = 4

xList = [-2,-1,0,1,2]
yList = [1,2,3,3,4]
N = 5

#sympy stuff
xList = Array(xList)
yList = Array(yList)
k = symbols('k', integer = True)
x, y, A, B, Eq2, s = symbols('x y A B Eq2(f) s')
x, y, f = IndexedBase("x"), IndexedBase("y"), IndexedBase("f")

#printing out the normal equations
sum1 = Sum(x[k]**2, (k, 1, N))
sum2 = Sum(x[k], (k, 1, N))
sum3 = Sum(x[k]*y[k], (k, 1, N))
pprint(Eq(A*sum1+B*sum2,sum3))

sum4 = Sum(y[k], (k, 1, N))
pprint(Eq(B*sum2+N*B,sum4))

xk = summation(xList[k], (k, 0, N-1))
yk = summation(yList[k], (k, 0, N-1))
xk2 = summation(xList[k]**2, (k, 0, N-1))
xkyk = summation(xList[k]*yList[k], (k, 0, N-1))

normal1 = Eq(xk2*A + xk*B, xkyk, evaluate=False)
normal2 = Eq(xk*A + N*B, yk, evaluate=False)

sol = solve((normal1,normal2),(A,B))

#printing out the normal equations with values
factor = xk/N

pprint(Eq(xk2*A + xk*B, xkyk, evaluate=False))
pprint(Eq(xk*A + N*B, yk, evaluate=False))
pprint(Eq((xk2-factor*xk)*A, (xkyk-factor*yk), evaluate=False))
pprint(Eq(A, (xkyk-factor*yk)/(xk2-factor*xk), evaluate=False))
pprint(Eq(B, (yk-xk*sol[A])/N, evaluate=False))

print("A = ",float(sol[A]), ", B = ",float(sol[B]))

fun = float(sol[A])*x + float(sol[B])
pprint(Eq(y, fun, evaluate=False))

#--------------Root Mean Square Error-------------
fx = summation(((float(sol[A])*xList[k] + float(sol[B])-yList[k]))**2, (k, 0, N-1))
with evaluate(False):
    rmse = ((1/N)*Sum((f[k] - y[k])**2, (k, 1, N)))**(1/2)
    pprint(Eq(Eq2, rmse, evaluate=False))
    pprint(Eq(Eq2, (fx*(1/N))**(1/2)))
print(Eq2, "=", ((fx*(1/N))**(1/2)).round(roundF))

#-------------------Table for Sum-----------------
TableSum = []
tempList = []
for val in xList:
    tempList.append(val)
tempList.append(xk)
TableSum.append(list(tempList))

tempList.clear()
for val in yList:
    tempList.append(val)
tempList.append(yk)
TableSum.append(list(tempList))

tempList.clear()
for val in xList:
    tempList.append(val**2)
tempList.append(xk2)
TableSum.append(list(tempList))

tempList.clear()
for valx,valy in zip(xList,yList):
    tempList.append(valx*valy)
tempList.append(xkyk)
TableSum.append(list(tempList))

roundF = 2

tempList.clear()
for valx in xList:
    tempList.append(round((float(sol[A])*valx + float(sol[B])),roundF))
tempList.append(sumList(tempList))
TableSum.append(list(tempList))

tempList.clear()
for valx,valy in zip(xList,yList):
    tempList.append(round(((float(sol[A])*valx + float(sol[B]))-valy),roundF))
tempList.append(sumList(tempList))
TableSum.append(list(tempList))

tempList.clear()
for valx,valy in zip(xList,yList):
    tempList.append(round((((float(sol[A])*valx + float(sol[B]))-valy)**2),roundF))
tempList.append(round(fx,roundF))
TableSum.append(list(tempList))
printTable(TableSum)