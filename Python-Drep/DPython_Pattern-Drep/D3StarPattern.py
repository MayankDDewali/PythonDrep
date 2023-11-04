"""
    *********
     *******
      *****
       ***
        *
"""


#For getting the number of rows
n = int(input("Enter the number of rows you want: "))

for i in range(n, 0, -1):               #For making the rows in descending order

    for j in range(n-i,0,-1):                   #For making the spaces
        print(" ", end="")
        
    for k in range(2*i-1, 0, -1):                   #For making the stars
        print("*", end="")
        
    print("")                           #For changing the rows