"""
                                      *                                   *
                                    *   *                               *   *
                                  *       *                           *       *
                                *           *                       *           * 
                              *               *                   *               *
                            *                   *               *                   *
                          *                       *           *                       *
                        *                           *       *                           *
                      *                               *   *                               * 
                    *                                   *                                   *
                      *                               *   *                               *
                        *                           *       *                           *
                          *                       *           *                       *
                            *                   *               *                   * 
                              *               *                   *               *
                                *           *                       *           *
                                  *       *                           *       *
                                    *   *                               *   *
                                      *                                   *
"""


x = int(input("Enter the number: "))

for i in range(1,x+1):
    
    for j in range(1,x-i+1):
        print(" ",end=" ")
        
    for k in range(1,2*i):
        if(k==1 or k==2*i-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    for j in range(1,2*(x-i)):
        print(" ",end=" ")
        
    for k in range(1,2*i):
        # if(i==x and k==2*x-2):
        #     continue
        # else:
        if(i==x and k==1):
            continue
        else:
            if(k==1 or k==2*i-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            
    print()
    
for i in range(x-1,0,-1):
    
    for j in range(1,x-i+1):
        print(" ",end=" ")
        
    for k in range(1,2*i):
        if(k==1 or k==2*i-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    for j in range(1,2*(x-i)):
        print(" ",end=" ")
        
    for k in range(1,2*i):
        # if(i==x and k==2*x-2):
        #     continue
        # else:
        if(i==x and k==1):
            continue
        else:
            if(k==1 or k==2*i-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            
    print()