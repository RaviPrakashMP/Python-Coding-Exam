import random
login_no = random.randint(1,25)

counter = 0
while counter < 3:
    counter += 1

    guess_login_no = int(input("Enter a number:"))

    if guess_login_no == login_no:
        print("Welcome!!!")
        break

    elif guess_login_no < login_no-2:
        print("invalid passcode")
        

    elif guess_login_no > login_no+2:
        print("INVALID PASSCODE")
        

    elif guess_login_no <= login_no+2 and guess_login_no >= login_no-2:
        print("InVaLiD PaSsCoDe")
        counter -= 1

while counter >= 3:
    counter += 1

    guess_login_no = int(input("Enter a number:"))
    
    if guess_login_no == login_no:
        print("Welcome!!!")
        break
    

    elif guess_login_no < login_no-2:
        print("LOGIN FAILED!!!")
        break
    

    elif guess_login_no > login_no+2:
        print("LOGIN FAILED!!!")
        break
    

    elif guess_login_no <= login_no+2 and guess_login_no >= login_no-2:
       print("LOGIN FAILED!!!")
       break

    

    
        
    
    
