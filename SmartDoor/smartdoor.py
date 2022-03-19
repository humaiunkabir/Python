defaut_Password = "open@"
fav_color = "black" 
def smartDoorCheckPass(defaut_Password, fav_color):
    i=1
    while i <= 3:
        password = input("Please Enter Smart Door Password For Open The Door: ")
        if(password==defaut_Password):
            print("Smart Door Is Opened!")
            break
        else:
            print("Smart Door Password Is Incorrect. Please Try Again.")
            if(i == 3):
                print("Security Question!")
                security_question=input("What is your favourite color? ")
                if(fav_color==security_question):
                    defaut_Password = input("Please reset your password: " )
                    smartDoorCheckPass(defaut_Password, fav_color)
                else:
                    print("Your Favourite Color Not Matched. Finally Smart Door Is Locked!")
                    break
        i=i+1

smartDoorCheckPass(defaut_Password,fav_color)
    


