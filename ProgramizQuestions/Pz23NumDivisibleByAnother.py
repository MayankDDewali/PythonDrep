# Pz23- Python Program to Find Numbers Divisible by Another Number

li = []         # Making an empty list

limit = int(input("How many numbers would you like to include: "))      # For getting number of inputs

for i in range(limit):
    num = int(input("Enter the {} number: ".format(i)))         # For getting the numbers
    li.append(num)                      # For adding the numbers into the empty list

x = int(input("Please enter the number you'd like to check for divisibility: "))    # For getting the num that will divide

li2 = []                # Creating another list
for i in li:
    if(i%x==0):         # Checking wether the first list's numbers can be devided by the given number
        li2.append(i)   # For storing numbers into the second list
    else:
        continue
print("Numbers divisible by",x," are ",li2)

# Made by MayankDd