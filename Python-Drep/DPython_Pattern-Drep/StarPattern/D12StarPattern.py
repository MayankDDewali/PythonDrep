"""
                          * 
                        *   * 
                      *       * 
                    *           * 
                  *               * 
                *                   * 
              *                       * 
            *                           * 
          *                               * 
        *                                   * 
          *                               * 
            *                           * 
              *                       * 
                *                   * 
                  *               * 
                    *           * 
                      *       * 
                        *   * 
                          *
"""

#For getting the number of rows
n = int(input("Enter the number of rows: "))

for i in range(1,n+1):                      #For making different rows in ascending order
    
    for j in range(n-i,0,-1):
        print(" ", end=" ")
    
    for k in range(1,i*2):                  #For making stars
        
#Giving conditions so that this will print stars in first and last of the line and at last row
        
        if(k==1 or k==i*2-1):           #This will print star
            print("*",end=" ")
            
        else:                               #This will print spaces
            print(" ",end=" ")
            
    print("")

for i in range(n-1,0,-1):                      #For making different rows in ascending order
    
    for j in range(n-i,0,-1):
        print(" ", end=" ")
    
    for k in range(1,i*2):                  #For making stars
        
#Giving conditions so that this will print stars in first and last of the line and at last row
        
        if(k==1 or k==i*2-1 or i==n):           #This will print star
            print("*",end=" ")
            
        else:                               #This will print spaces
            print(" ",end=" ")
            
    print("")