from random import randint
from random import choice

options = ["R", "P", "S"]

def choice():
    return options[randint(0,2)]
output = choice()


def game():
    userinput = False
    if userinput == False:
        userinput = input("R, P, S: \n")
        userinput = userinput.lower()
        userinput = userinput.capitalize()
        if userinput == output:
            print("Tie")
            print("Please try again")
            choice()
            game()
        elif userinput == "R":
            if output == "P":
                print("Player choose", userinput, "Computer choose", output)
                print("You loose!", output, "covers", userinput)
            else:
                print("Player choose", userinput, "Computer choose", output)

                print("You win!", userinput, "smashes", output)
        elif userinput == "P":
            if output == "S":
                print("Player choose", userinput, "Computer choose", output)

                print("Player loose!", output, "cuts", userinput)
            else:
                print("Player choose", userinput, "Computer choose", output)
                print("You win!", userinput, "covers", output)
        elif userinput == "S":
            if output == "R":
                print("Player choose", userinput, "Computer choose", output)
                print("Player loose!", output, "smashes", userinput)
            else:
                print("Player choose", userinput, "Computer choose", output)
                print("Player win!", userinput, "cut", output)
        else:
            print("Thats not a valid play, Check your spelling!")
            print("Please try again")
            choice()
            game()
            
game()  

