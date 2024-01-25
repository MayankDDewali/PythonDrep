# Pz26- Python Program to Find HCF or GCD

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

if(x==y):
    print("HCF of",x,"and",y,"is ",x)
else:
    if(x>y):
        xm = y
    else:
        xm = x

    for i in range(1, xm):
        if(x%i==0 and y%i==0):
            hcf = i
        else:
            continue

    print("HCF of",x,"and",y,"is ",hcf)