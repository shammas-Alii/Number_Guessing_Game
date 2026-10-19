import random
def play_game():

    while True:
        print ("-------HI WELCOME TO NUMBER GUESSING GAME-------")
        print("Please Select Dificulty Mode:")
        print("1:Easy mode (1,50)")
        print("2:Medium mode (1,100)")
        print("3:Hard mode (1,200)")
        choice = input("Please Enter Your Choice:(1, 2 or 3) :")


        if(choice=='1'):
            max_range = 50
            break
        elif(choice=='2'):
            max_range = 100
            break
        elif(choice=='3'):
            max_range = 200
            break
        else:
            print("Please enter a valid number between (1 , 2 , 3)")
        

    computerchoice = random.randint(1,max_range)

    attempts = 0
    print(f"I chose a random number between 1 and {max_range} ")
    print("lets start this game")


    while True:

        try:
                userchoise=int(input("Please enter you number : "))
                attempts += 1
                if userchoise<computerchoice:
                    print("This number is lower then my guess. Please try Higher number")
                elif userchoise>computerchoice:
                    print("This number is greater then my guess. Please try Lower number ")
                else:
                    print(f"AMAZING YOU GUESSED THE RIGHT NUMBER IN {attempts} ATTEMPTS")
                    break
        except ValueError:
                print("Please enter the right integer (number) to play this game")


while True:
    play_game()
    replay = input("Do you want to again (Yes/No)").strip().upper()
    if replay != 'Y':    
        print("-------GAME IS ENDED , THANKS FOR PLAYING-------")
        break
print("\n" + "="*40 + "\n")

