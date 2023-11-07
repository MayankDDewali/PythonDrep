#How to swap value of two numbers


#For getting the numbers
a = int(input("Enter the first value: "))

b = int(input("Enter the second value: "))

print("Before Swapping")
print("Value of a = ", a)
print("Value of b = ", b)
print("")
#For swapping the numbers
a, b = b, a

print("After swapping")
print("Value of a = ", a)
print("Value of b = ", b)