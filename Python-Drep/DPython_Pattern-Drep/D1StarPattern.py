"""
                *****
                ****
                ***
                **
                *
"""


#For getting the number of rows
n = int(input("Enter the number of rows you want: "))

for i in range(n,0,-1):             #For making different rows in descending order

    for j in range(i,0,-1):            #For making the stars
        print("*",end="")
        
    print("")                       #For changing the rows