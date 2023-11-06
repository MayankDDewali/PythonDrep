"""
                12345
                1234
                123
                12
                1
"""

#For making the number of rows
n = int(input("Enter the number of rows you want: "))

for i in range(n,0,-1):             #For making the number of rows in descending order
    
    for j in range(1,i+1):          #For making the numbers
        print(j,end="")
        
    print("")                       #For changing the rows