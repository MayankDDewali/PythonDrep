# Pz23- Python Program to Find Numbers Divisible by Another Number

li = []

limit = int(input("How many numbers would you like to include: "))

for i in range(limit):
    num = int(input("Enter the {} number: ".format(i)))
    li.append(num)

x = int(input("Please enter the number you'd like to check for divisibility: "))

li2 = []
for i in li:
    if(i%x==0):
        li2.append(i)
    else:
        continue
print("Numbers divisible by",x," are ",li2)