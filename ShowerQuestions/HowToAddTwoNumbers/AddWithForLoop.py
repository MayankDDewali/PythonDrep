# How to add two numbers by using for loop

# Asking for the input from the user
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# I have taken list
li = []

# Adding the "m" (or you can add anything) into list x times
for i in range(x):
    li.append("m")

# Adding the "m" (or you can add anything) into list y times
for i in range(y):
    li.append("m")

# At last printing the length of the list
print(len(li))