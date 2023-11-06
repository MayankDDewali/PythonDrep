"""
                   *
                  **
                 ***
                ****
                 ***
                  **
                   *
"""

#For getting the number of rows
n = int(input("Enter the number of rows: "))

for i in range(0,n):                #For making different rows in ascending order
    
    for j in range(n-i):            #For giving spaces in descending
        print(" ",end="")
        
    for k in range(0,i):            #For making stars in ascending order
        print("*",end="")
    
    print("")                       #For changing the rows

for i in range(0,n):                #For making different rows in descending order
    
    for j in range(n-i):            #For giving spaces in ascending order
        print(" ",end="")
        
    for k in range(0,i):            #For making stars in descending order
        print("*",end="")
    
    print("")                       #For changing the rows