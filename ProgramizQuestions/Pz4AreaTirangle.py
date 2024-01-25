# Pz4- Python Program to Calculate the Area of a Triangle


def funct():
    #For getting the first number
    a = int(input("Enter the first side of the triangle: "))
    #For getting the second number
    b = int(input("Enter the second side of the triangle: "))
    #For getting the third number
    c = int(input("Enter the third side of the triangle: "))
    if(a<=0 or b<=0 or c<=0):                                        #Giving conditions for invalid sides
        print("Please only enter the positive number.")
        funct()                                                 #For recalling the function
    elif(a+b<=c or b+c<=a or a+c<=b):                            #Giving conditions for invalid sides
        print("You have provided invalid sides")
    else:
        s = (a+b+c)/2                                           ##For calculating the 1/2 of perimeter
        area = (s*(s-a)*(s-b)*(s-c))**.5                        #Area of triangle
        print("Area of triangle = %.4f" %area)
funct()

# Made by MayankDd