# Pz18- Python Program to Print the Fibonacci sequence


def FiboFunc():                                                     
    n = int(input("Enter the number of sequence you want: "))
    n1=0                    # First Number
    n2=1                    # Second Number

    if(n<=0):                                               # Condition for invalid input
        print("Please enter the positive number only")
        FiboFunc()
    elif(n==1):                     # Condition for geting first number if input is 1
        print(n1)
    else:                           # For getting the fibonacci sequence in given range
        for i in range(1,n+1):
            print(n1)
            temp=n1
            n1=n2
            n2=temp+n2
FiboFunc()

# Made by MayankDd