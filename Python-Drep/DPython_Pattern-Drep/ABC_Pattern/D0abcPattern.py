"""
                A
                AB
                ABC
                ABCD
                ABCDE
"""
#For getting the number of rows
n= int(input("Enter the number of rows you want: "))
for i in range(1,n+1):                #for making different rows in ascending order
    
    for j in range(1,i+1):          #For starting ABC...
        print(chr(64+j),end="")
        
    print("")                       #For changing lines