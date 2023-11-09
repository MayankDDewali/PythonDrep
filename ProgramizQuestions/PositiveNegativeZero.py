#Python Program to Check if a Number is Positive, Negative or 0


n = int(input("Enter the number: "))                #For getting the value of n

#Giving conditions to get the output
if(n < 0):
    print(n," is a negative number.")

elif(n > 0):
    print(n," is a positive number.")

else:
    print(n," is 0")