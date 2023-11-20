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
            fact = 0
            x = i
            
            while x != 0:
                r = x % 10
                x = x // 10
                fact = fact + r**3
                
            if fact == i:
                Found = True  # Setting value to True if armstrong are found
                print(i)
        if not Found:
            print("There are no Armstrong numbers between range",n1,"to",n2,".")
Armstrong()