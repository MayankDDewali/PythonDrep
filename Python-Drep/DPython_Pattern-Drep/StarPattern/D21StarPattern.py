"""
                                  * 
                                * * * 
                              * * * * * 
                            * * * * * * * 
                          * * * * * * * * * 
                        * * * * * * * * * * * 
                      * * * * * * * * * * * * * 
                    * * * * * * * * * * * * * * * 
                  * * * * * * * * * * * * * * * * * 
                * * * * * * * * * * * * * * * * * * * 
                  * * * * * * * * * * * * * * * * * 
                    * * * * * * * * * * * * * * * 
                      * * * * * * * * * * * * * 
                        * * * * * * * * * * * 
                          * * * * * * * * * 
                            * * * * * * * 
                              * * * * * 
                                * * *
                                  *
"""


#For getting the number of rows
n = int(input("Enter the number of rows you want: "))

for i in range(0,n+1):              #For making the rows in ascending order

    for j in range(0,n-i):        #For making spaces
        print(" ",end=" ")
        
    for k in range(1,2*i):          #For making stars
        if(k==1 or k==2*i-1):
            print("*",end=" ")
        else:
            if(i%2==0 and k%4==0) or (i%5==0 and (k%4==0 or k%6==0) or k==n):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        
    print("")                       #For changing the rows

for i in range(n-1, 0, -1):               #For making the rows in descending order

    for j in range(n-i,0,-1):                   #For making the spaces
        print(" ", end=" ")
        
    for k in range(2*i-1, 0, -1):                   #For making the stars
        if(k==1 or k==2*i-1):
            print("*",end=" ")
        else:
            if(i%2==0 and k%4==0) or (i%5==0 and (k%4==0 or k%6==0) or k==n):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        
    print("")                           #For changing the rows