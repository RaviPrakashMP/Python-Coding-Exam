#Ask the user to enter a 3 digit number till he enters 0
#Print the square root of only 3 digit positive numbers.
#Make sure that the program does not
#print the square root of any number that is not a 3 digit number

num = []

while True:
    num1 = int(input("Enter a 3 digit number:"))
    num.append(num1)
    
    if num1 == 0:
        break

    elif 99 < num1 < 999:
        print(num1**0.5)

    else:
        print("The entered number is not a 3 digit numner")
    
