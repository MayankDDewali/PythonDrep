# Python Program to Find Armstrong Number in an Interval
n1 = int(input("Enter the starting point: "))
n2 = int(input("Enter the ending point: "))

for i in range(n1,n2+1):
    fact = 0
    x = i
    while(x!=0):
        r=x%10
        x = x//10
        fact=fact+r**3
    if(fact==i):
        print(i)
    else:
        continue