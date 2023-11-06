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
n = int(input("Enter the number of rows you want: "))

for i in range(0,n):                #For making different rows in ascending order
    
    for j in range(0,i+1):          #For making stars in ascending order
        print("*",end="")
        
    print("")                       #For changing the rows
    
for i in range(n,0,-1):             #For making different rows in descending order
    
    for j in range(0,i-1):          #For making stars in descending order
        print("*",end="")
        
    print("")                       #For changing the rows