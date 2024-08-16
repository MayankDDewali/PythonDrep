"""
                * * * * * * * * * *
                *               *
                *             *
                *           *
                *         *
                *       *
                *     *
                *   *
                * *
                *
"""

#For getting the number of rows
n = int(input("Enter the number of rows: "))

for i in range(n,0,-1):                      #For making different rows in descending order
    
    for j in range(1,i+1):                  #For making stars
        
#Giving conditions so that this will print stars in first and last of the line and at last row
        
        if(j==1 or j==i or i==n):           #This will print star
            print("*",end=" ")
            
        else:                               #This will print spaces
            print(" ",end=" ")
            
    print("")