# Pz20- Python Program to Find Armstrong Number in an Interval

def Armstrong():
    n1 = int(input("Enter the starting point: "))
    n2 = int(input("Enter the ending point: "))
    
    if n1 < 0 or n2 < 0 or n1 > n2:
        print("Please only write a non-decimal positive integer, and the starting point should be smaller than the ending point...")
        Armstrong()
    else:
        Found = False  # This is for founding if the armstrong are found or not
        
        print("Armstrong numbers between range",n1,"to",n2,"are:")

        for i in range(n1, n2 + 1):
            arm = 0
            x = i
            
            while x != 0:
                r = x % 10              # For getting the last number(Ex- If x=123 then we'll get 3)
                x = x // 10             # For adding the sum of the cube of the digits
                arm = arm + r**3        # For making quotient the remainder
                
            if arm == i:
                Found = True  # Setting value to True if armstrong are found
                print(i)
        if not Found:
            print("There are no Armstrong numbers between range",n1,"to",n2,".")
Armstrong()

# Made by MayankDd