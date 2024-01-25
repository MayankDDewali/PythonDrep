# Pz14- Python Program to Check Prime Number


#For getting the number
num = int(input("Enter the number: "))
#Making a variable with the value 0
count = 0
#Making a for loop that will run from 2 to the given number
for i in range(2,num+1):
#Giving conditions for prime number
    if(num%i==0):
        count+=1                                #Incresing the value of count
    else:
        continue

#Giving conditions for printing prime or not
if(count==1):
    print(num," is the prime number.")
else:
    print(num," is not the prime number.")
    
# Made by MayankDd