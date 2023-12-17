# Pz22- Display the powers of 2 using anonymous function

# Asking for the power
pow = int(input("Enter the power: "))

# Making a lambda function (Anonymous function)
result = (lambda a, b : a**b) (2, pow)

print("2 to the power ",pow," = ",result)