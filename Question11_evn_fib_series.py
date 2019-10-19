#Write a Python program to print the first 12 "even" Fibonacci numbers.

#Assume Fibonacci numbers start from 1 and 1.

a = 1
b = 1
counter = 0
while counter < 17:
    a = a+b
    b = a+b
    counter += 1
    if a % 2 == 0:
        print(a)
    if b % 2 ==0:
        print(b)

    
