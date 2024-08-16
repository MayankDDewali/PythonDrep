# For printing this pattern...
"""
                            * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
                              * * * * * * * * * * * * * * * * *     * * * * * * * * * * * * * * * * * 
                                * * * * * * * * * * * * * * *         * * * * * * * * * * * * * * * 
                                  * * * * * * * * * * * * *             * * * * * * * * * * * * * 
                                    * * * * * * * * * * *                 * * * * * * * * * * * 
                                      * * * * * * * * *                     * * * * * * * * * 
                                        * * * * * * *                         * * * * * * * 
                                          * * * * *                             * * * * * 
                                            * * *                                 * * * 
                                              *                                     *
"""


#For getting the number of rows
x = int(input("Enter the number: "))

for i in range(x,0,-1):                                  # For making different rows in ascending order like this: (5,4,3,2,1)
    for j in range(1,x-i+1):                            # For giveing spaces in decending order like this: (0,1,2,3,4)
        print(" ",end=" ")
    for k in range(1,2*i):                              # For printing the stars in asscending odd order like this (9,7,5,3,1)
        print("*",end=" ")
    for l in range(1,2*(x-i)+1):                        # Again for pringing the spaces in descending even order like this (0,2,4,6,8)
        print(" ",end=" ")
    for k in range(1,2*i):                              # For pringing the stars in asscending odd order like this (9,7,5,3,1)
        print("*",end=" ")
    print()