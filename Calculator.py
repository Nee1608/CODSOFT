print ("~~~~~~~ MINI CALCULATOR ~~~~~~~")

number1 = float(input(" Enter first number here: "))
number2 = float(input(" Enter second number here: "))
choice = 0

while choice < 5 :

    print(" Press 1 for Addition \n Press 2 for Subtraction\n Press 3 for Multiplication\n Press 4 for Division\n Press 5 for Exit")

    choice = int(input(" Enter your choice here from 1-4: "))

    if choice == 1 :
        print(" The addition of given two numbers is: ",number1 + number2)
    elif choice == 2 :
        print(" The subtraction of given two numbers is: ",number1 - number2)
    elif choice == 3 :
        print(" The multiplication of given two numbers is: ",number1 * number2)
    elif choice == 4 :
        print(" The division of given two numbers is: ",number1 / number2)
    elif choice == 5 :
        break
    else :
        print(" Invalid Input!!! ")
