# Pz18- Python Program to Print the Fibonacci sequence


def FiboFunc():                                                     
    n = int(input("Enter the number of sequence you want: "))
    n1=0
    n2=1

    if(n<=0):
        print("Please enter the positive number only")
        FiboFunc()
    elif(n==1):
        print(n1)
    else:
        for i in range(1,n+1):
            print(n1)
            temp=n1
            n1=n2
            n2=temp+n2
FiboFunc()

# Made by MayankDd