# Pz8- Python Program to Convert Kilometers to Miles


def Kilometer():                                                #Making the function so that we can call it anytime
    kilo = int(input("Enter the kilometer value: "))            #For getting the value of kilometer
    if(kilo<=0):                                                #For invalid values
        if(kilo==0):
            print("0 miles")
        else:                                                   #For calling again if invalid
            print("Please only enter the valid ")
            Kilometer()
    else:
        mile = kilo * 0.621371                                  #Converting kilometers to mile
        print(kilo," kilometers = %.4f miles"%mile)
Kilometer()                                                     #Calling the function