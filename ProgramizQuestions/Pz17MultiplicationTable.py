# Pz17- Python Program to Display the multiplication Table


n = int(input("Enter the number: "))            #For getting the value
print("Multiplication of ",n," is:")
for i in range(1,11):                           #For printing the multiplication of the given number
    print(n," * ",i," = ",n*i)