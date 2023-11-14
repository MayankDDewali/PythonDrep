#Python Program to Check Armstrong Number
num = int(input("Enter the number: "))
x=num
arm=0
while(x!=0):
    r=x%10
    arm=arm+r**3
    x=x//10
if(arm==num):
    print(num," is an armstrong number.")
else:
    print(num," is not an armstrong number.")