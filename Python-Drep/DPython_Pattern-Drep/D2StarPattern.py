#For getting the number of rows
n = int(input("Enter the number of rows you want: "))

for i in range(0,n+1):              #For making the rows in ascending order

    for j in range(0,n-i+1):        #For making spaces
        print(" ",end="")
        
    for k in range(1,2*i):          #For making stars
        print("*",end="")
        
    print("")                       #For changing the rows