# Pz21- ython Program to Find the Sum of Natural Numbers

def SumNumbers():
    num = int(input("Enter the natural number: "))      # For getting the number from the user
    sum = 0

    if(num<=0):                                         # 
        print("Please write only positive numbers")
        SumNumbers()
    else:
        while(num!=0):
            sum+=num
            num-=1
        print(sum)
SumNumbers()