from sympy import *

#----------------------Function-------------------
def stringToIntList(List1):
    List2 = []
    for ch in List1:
        List2.append(int(ch))
    return List2

def sumList(list1):
    sumVal = 0
    for val in list1:
        sumVal+=val
    return sumVal
    
def printList(list1):
    for row in list1:
        print(row)
    print('')

def printTable(list1):
    f = open("output2.csv", "w")
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
x, y = symbols('x y')
roundF = 4

xList = [1,2,3]
yList = [0.2,2,6]
M = 2
N = 3

xList = Array(xList)
yList = Array(yList)

#-------------------Sympy Stuff-------------------
k = symbols('k', integer = True)
A, B, Eq2, s = symbols('A B Eq_2(f) s')
x = IndexedBase("x")
y = IndexedBase("y")
f = IndexedBase("f")

#--------Printing Out the Normal Equations--------
sum1 = Sum(x[k]**M*y[k], (k, 1, N))
sum2 = Sum(x[k]**(2*M), (k, 1, N))
pprint(Eq(A, sum1/sum2))

xkyk = summation(xList[k]**M*yList[k], (k, 0, N-1))
xk2 = summation(xList[k]**(2*M), (k, 0, N-1))

normal1 = Eq(A, xkyk/xk2, evaluate=False)

#--Printing Out the Normal Equations with Values--
pprint(normal1)

sol = solve(normal1,A)
print("A = ",round(float(sol[0]),roundF))

fun = sol[0]*x**M
pprint(Eq(y, fun, evaluate=False))

fx = summation(((sol[0]*xList[k]**M - yList[k])**2), (k, 0, N-1))

#--------------Root Mean Square Error-------------
with evaluate(False):
    rmse = ((1/N)*Sum((A*x[k]**M - y[k])**2, (k, 1, N)))**(1/2)
    pprint(Eq(Eq2, rmse, evaluate=False))
    pprint(Eq(Eq2, ((1/N)*fx)**(1/2)))
pprint(Eq(Eq2, ((1/N)*fx)**(1/2)))

#-------------------Table for Sum-----------------
TableSum = []
tempList = []
for val in xList:
    tempList.append(val)
tempList.append(sumList(tempList))
TableSum.append(list(tempList))

tempList.clear()
for val in yList:
    tempList.append(val)
tempList.append(sumList(tempList))
TableSum.append(list(tempList))

tempList.clear()
for valx,valy in zip(xList,yList):
    tempList.append((valx**M)*valy)
tempList.append(sumList(tempList))
TableSum.append(list(tempList))

tempList.clear()
for val in xList:
    tempList.append(val**(2*M))
tempList.append(sumList(tempList))
TableSum.append(list(tempList))

roundF = 2

tempList.clear()
for valx in xList:
    tempList.append(round((sol[0]*valx**M),roundF))
tempList.append(sumList(tempList))
TableSum.append(list(tempList))

tempList.clear()
for valx,valy in zip(xList,yList):
    tempList.append(round((sol[0]*valx**M - valy),roundF))
tempList.append(sumList(tempList))
TableSum.append(list(tempList))

tempList.clear()
for valx,valy in zip(xList,yList):
    tempList.append(round(((sol[0]*valx**M - valy)**2),roundF))
tempList.append(round(fx,roundF))
TableSum.append(list(tempList))
printTable(TableSum)