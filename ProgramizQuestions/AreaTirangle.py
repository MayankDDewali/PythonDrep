#How to find the area of triangle


#For getting the first number
a = int(input("Enter the first side of the triangle: "))

#For getting the second number
b = int(input("Enter the second side of the triangle: "))

#For getting the third number
c = int(input("Enter the third side of the triangle: "))

#For calculating the 1-2 of perimeter
s = (a+b+c)/2

#Area of triangle
area = (s*(s-a)*(s-b)*(s-c))**.5

print("Area of triangle = %.4f" %area)