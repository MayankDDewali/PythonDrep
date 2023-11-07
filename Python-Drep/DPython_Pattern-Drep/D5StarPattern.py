"""
                *****
                *   *
                *   *
                *   *
                *****
"""


#For getting the number of rows
n = int(input("Enter the number of rows you want: "))

for i in range(0,n):                    #For making different rows in ascending order
    
    if(i==0 or i==n-1):                 #Giving conditions to print star between firsst and last row
        print("*" * n)
        
    else:
        print("*" + " "*(n-2) + "*")