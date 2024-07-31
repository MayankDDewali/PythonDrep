# How to add two numbers without the help of any operator

# Asking for the input from the user
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# I have taken string you can take the list
string = ""

# Adding the "m" (or you can add anything) into string x times
for i in range(x):
    string+="m"

# Adding the "m" (or you can add anything) into string y times
for i in range(y):
    string+="m"

# At last printing the length of the string
print(len(string))