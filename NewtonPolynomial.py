#----------------------Function-------------------
# Function to find the product term 
def proterm(i, value, x): 
    pro = 1; 
    for j in range(i): 
        pro = pro * (value - x[j]); 
    return pro; 
  
# Function for calculating 
# divided difference table 
def dividedDiffTable(x, y, n):
  
    for i in range(1, n): 
        for j in range(n - i): 
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j]));
    return y;
  
# Function for applying Newton's 
# divided difference formula 
def applyFormula(value, x, y, n): 
  
    sum = y[0][0]; 
  
    for i in range(1, n):
        sum = sum + (proterm(i, value, x) * y[0][i]); 
      
    return sum; 
  
# Function for displaying divided 
# difference table 
def printDiffTable(y, n): 
  
    for i in range(n): 
        for j in range(n - i): 
            print(round(y[i][j], 4), "\t", 
                               end = " "); 
        print(""); 

#-----------------------Main----------------------
# Driver Code
  
# number of inputs given 
n = 4;
M = 10
y = [[0 for i in range(M)] 
        for j in range(M)];
xList = [0,1,2,3]
  
# y[][] is used for divided difference 
# table where y[][0] is used for input 
y[0][0] = 0;
y[1][0] = -1;
y[2][0] = 12;
y[3][0] = 75;
#y[4][0] = 64;
  
# calculating divided difference table 
y=dividedDiffTable(xList, y, n); 
  
# displaying divided difference table 
printDiffTable(y, n); 
  
# value to be interpolated 
value = 0.8; 
  
# printing the value 
print("\nValue at", value, "is",
        round(applyFormula(value, xList, y, n), 2))