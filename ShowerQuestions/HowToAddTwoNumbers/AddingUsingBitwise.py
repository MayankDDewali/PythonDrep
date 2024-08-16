# This question is for practice and to demonstrate my understanding of Python and my ability to solve various problems.

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

z = x | y
z = z<<1

print(z)


x = int(input("Enter the number: "))
for i in range(0,x):
    for j in range(0,x-i):
        print(" ",end="")
    for k in range(0,2*i+1):
        print("*",end="")
    print()