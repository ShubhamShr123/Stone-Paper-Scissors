import random

def stonepaperscissors():
    try:
        count = 0
        pcwin = 0
        userwin = 0
        element = ["Stone", "Paper", "Scissors"]
        while(count<=11):
            count+=1
            if count==9:
                print(f"You won {userwin} times and PC won {pcwin} times")
                if pcwin>userwin:
                    print("PC is the winner")
                    break
                elif pcwin<userwin:
                    print("You are  the winner")
                    break
                else:
                    print("Draw !!")
                    break

            pcchoice = random.choice(element)
            userchoice = int(input("0 for stone, 1 for paper, 2 for scissors : "))

            if pcchoice==element[0]:
                if userchoice==1:
                    userwin+=1
                    print(f"{pcchoice} vs {element[userchoice]}")
                    print(f"You won\nYou have {-count+9} moves left")
                    print(f"Your points are {userwin} and Pc points are {pcwin}")
                    print()
                    continue
                elif userchoice==2:
                    pcwin+=1
                    print(f"{pcchoice} vs {element[userchoice]}")
                    print(f"Computer wins\nYou have {-count+9} moves left")
                    print(f"Your points are {userwin} and Pc points are {pcwin}")
                    print()
                    continue
                elif userchoice==0:
                    print(f"{pcchoice} vs {element[userchoice]}")
                    print(f"Draw\n{-count+9} moves left")
                    print(f"Your points are {userwin} and Pc points are {pcwin}")
                    print()
                    continue
                
            if pcchoice==element[1]:
                if userchoice==0:
                    pcwin+=1
                    print(f"{pcchoice} vs {element[userchoice]}")
                    print(f"Computer wins\nYou have {-count+9} moves left")
                    print(f"Your points are {userwin} and Pc points are {pcwin}")
                    print()
                    continue
                elif userchoice==1:
                    print(f"{pcchoice} vs {element[userchoice]}")
                    print(f"Draw\n{-count+9} moves left")
                    print(f"Your points are {userwin} and Pc points are {pcwin}")
                    print()
                    continue
                elif userchoice==2:
                    userwin+=1
                    print(f"{pcchoice} vs {element[userchoice]}")
                    print(f"You win\nYou have {-count+9} moves left")
                    print(f"Your points are {userwin} and Pc points are {pcwin}")
                    print()
                    continue
                
            if pcchoice==element[2]:
                if userchoice==0:
                    userwin+=1
                    print(f"{pcchoice} vs {element[userchoice]}")
                    print(f"You won\nYou have {-count+9} moves left")
                    print(f"Your points are {userwin} and Pc points are {pcwin}")
                    print()
                    continue
                elif userchoice==1:
                    pcwin+=1
                    print(f"{pcchoice} vs {element[userchoice]}")
                    print(f"Computer wins\nYou have {-count+9} moves left")
                    print(f"Your points are {userwin} and Pc points are {pcwin}")
                    print()
                    continue
                elif userchoice==2:
                    print(f"{pcchoice} vs {element[userchoice]}")
                    print(f"Draw\n{-count+9} moves left")
                    print(f"Your points are {userwin} and Pc points are {pcwin}")
                    print()
                    continue
    except IndexError:
        print("Please enter numbers only between (0, 1, 2)")
    except ValueError:
        print("Value eneterd is not an integer")

stonepaperscissors()
    