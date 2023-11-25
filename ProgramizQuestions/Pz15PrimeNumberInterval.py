# Pz15- Python Program to Print all Prime Numbers in an Interval


first = int(input("Enter the starting point: "))

last = int(input("Enter the ending point: "))
print("Prime numbers are:")
for i in range(first, last+1):
    count = 0                                       #For initializing
    for j in range(2,i+1):
#Giving conditions for prime number
        if(i%j==0):
            count+=1                                #Incresing the value of count
        else:
            continue

#Giving conditions for printing prime or not
    if(count==1):
        print(i," is the prime number.")
    else:
        continue