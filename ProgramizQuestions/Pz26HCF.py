# Pz26- Python Program to Find HCF or GCD

x = int(input("Enter the first number: "))          # For getting the first number
y = int(input("Enter the second number: "))         # For getting the second number

if(x==y):                                           # Checking wether the numbers are equal
    print("HCF of",x,"and",y,"is ",x)
else:                                               # Condition for getting the smallest num among those
    if(x>y):
        xm = y
    else:
        xm = x

    for i in range(1, xm):                          # Getting the biggest number that can devide both num
        if(x%i==0 and y%i==0):
            hcf = i
        else:
            continue

    print("HCF of",x,"and",y,"is ",hcf)
    
# Made by MayankDd