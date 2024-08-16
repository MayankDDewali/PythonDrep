"""
                1
                12
                123
                1234
                12345
"""

#This is for getting the number of rows
n = int(input("Enter the number of rows you want: "))

for i in range(1,n+1):              #For making different rows in ascending order
    
    for j in range(1,i+1):          #For starting the numbers from 1
        print(j,end="")
        
    print("")                       #For changing the rows