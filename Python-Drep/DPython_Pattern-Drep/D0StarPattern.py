#For getting the number of rows
n= int(input("Enter the number of rows you want: "))

for i in range(0,n):                #for making different rows in ascending order

    for j in range(0,i+1):          #For making stars
        print("*", end="")
        
    print("")                       #For changing lines