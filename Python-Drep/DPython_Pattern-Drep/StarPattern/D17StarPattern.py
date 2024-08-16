# For printing this pattern...

"""
                            * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                              * * * * * * * * * * * * * * * * *   * * * * * * * * * * * * * * * * *
                                * * * * * * * * * * * * * * *       * * * * * * * * * * * * * * *
                                  * * * * * * * * * * * * *           * * * * * * * * * * * * *
                                    * * * * * * * * * * *               * * * * * * * * * * *
                                      * * * * * * * * *                   * * * * * * * * *
                                        * * * * * * *                       * * * * * * *
                                          * * * * *                           * * * * *
                                            * * *                               * * *
                                              *                                   *
"""



import time

#For getting the number of rows
x = int(input("Enter the number: "))

for i in range(x,0,-1):                                  # For making different rows in ascending order like this: (5,4,3,2,1)
    for j in range(1,x-i+1):                            # For giveing spaces in decending order like this: (0,1,2,3,4)
        print(" ",end=" ")
    for k in range(1,2*i):                              # For printing the stars in asscending odd order like this (9,7,5,3,1)
        print("*",end=" ")
        # time.sleep(.2)
    for l in range(1,2*(x-i)):                        # Again for pringing the spaces in descending even order like this (0,1,3,5,7)
        print(" ",end=" ")
    for k in range(1,2*i):                              # For pringing the stars in asscending odd order like this (9,7,5,3,1)
        if(k==2*x-1):                                 # Condition for printing the last line with 1 less star so that it'll look like both traingles have common star
            continue
        else:
            # time.sleep(.2)
            print("*",end=" ")
        # print("*",end=" ")
    time.sleep(.4)
    print()