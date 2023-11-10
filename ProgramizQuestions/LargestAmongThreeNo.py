#Python Program to Find the Largest Among Three Numbers


#To get three numbers...
a = int(input("Enter the first number: "))

b = int(input("Enter the second number: "))

c = int(input("Enter the third number: "))

#Condition for finding the largest number...
if(a>=b and a>=c):
    print(a," is the largest number.")
elif(b>=a and b>=c):
    print(b," is the largest number.")
else:
    print(c," is the largest number.")