# Pz19- Python Program to Check Armstrong Number

num = int(input("Enter the number: "))
x=num
arm=0
while(x!=0):
    r=x%10                      # For getting the last number(Ex- If x=123 then we'll get 3)
    arm=arm+r**3                # For adding the sum of the cube of the digits
    x=x//10                     # For making quotient the remainder
if(arm==num):                   # For checking the number
    print(num," is an armstrong number.")
else:
    print(num," is not an armstrong number.")
    
# Made by MayankDd