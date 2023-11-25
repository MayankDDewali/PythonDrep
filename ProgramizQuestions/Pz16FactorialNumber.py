# Pz16- Python Program to Find the Factorial of a Number


def Factorial():
    n = int(input("Enter the number: "))        #For getting the number
    fact = 1                                    #For initializing the value
    if(n<=0):
        if(n==0):
            fact=1
        else:
            print("Please enter positive number only...")
            Factorial()
    else:
        for i in range(1,n+1):                  #For multiplying
            fact*=i
    print(fact)
Factorial()