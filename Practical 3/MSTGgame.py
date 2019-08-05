#Man Tiger Cow Grass Puzzle Game Pracs

def PlayGame(BankA, BankB):
    Lives = 3
    while BankA != ['', '', '', '']:
        print("At Bank A " + BankA[0] + BankA[1] + BankA[2] + BankA[3] + "are present.")
        print("At Bank B " + BankB[0] + BankB[1] + BankB[2] + BankB[3] + "are present.")
        print("Lives Left With You " + str(Lives))
        Boat = ''
        print(
            "Please Enter Your Choice \n 1 - Man Goes Alone From Bank A To B \n 2 - Man Comes Back Alone From Bank B "
            "To Bank A \n 3 - Man Goes With Cow From Bank A To B \n 4 - Man Comes Back With Cow From Bank B To Bank A "
            "\n 5 - Man Goes With Tiger From Bank A To B \n 6 - Man Comes Back With Tiger From Bank B To Bank A \n 7 "
            "- Man Goes With Grass From Bank A To B \n 8 - Man Comes Back With Grass From Bank B To Bank A ")
        Choice = int(input("Your Choice Here Please"))
        if Choice == 1:
            if (BankA[2] != '') & (BankA[1] != ''):
                print("Cow Has Been Eaten By The Tiger")
                Lives = Lives - 1
            elif (BankA[2] != '') & (BankA[3] != ''):
                print("Grass Has Been Eaten By Cow")
                Lives = Lives - 1
            elif (BankA[0] == ''):
                print("Man Is Already At Bank B")
            else:
                BankB[0] = BankA[0]
                BankA[0] = Boat
        elif Choice == 2:
            if (BankB[2] != '') & (BankB[1] != ''):
                print("Cow Has Been Eaten By The Tiger")
                Lives = Lives - 1
            elif (BankB[2] != '') & (BankB[3] != ''):
                print("Grass Has Been Eaten By Cow")
                Lives = Lives - 1
            elif (BankB[0] == ''):
                print("Man Is Already At Bank A")
            else:
                BankA[0] = BankB[0]
                BankB[0] = Boat
        elif Choice == 3:
            if (BankA[0]!='') & (BankA[2]!=''):
                BankB[0] = BankA[0]
                BankB[2] = BankA[2]
                BankA[0] = Boat
                BankA[2] = Boat
                print("Cow has been transferred from Bank A to Bank B")
            elif BankA[0] == '':
                print("The Man Is Already At Bank B")
            elif BankA[2]== '':
                print("The cow is already at Bank B")
        elif Choice == 4:
            if (BankB[0]!='') & (BankB[2]!=''):
                BankA[0] = BankB[0]
                BankA[2] = BankB[2]
                BankB[0] = Boat
                BankB[2] = Boat
                print("Cow has been transferred from Bank B to Bank A")
            elif BankA[0] == '':
                print("The Man Is Already At Bank A")
            elif BankA[2]== '':
                print("The cow is already at Bank A")
        elif Choice == 5:
            if (BankA[2] != '') & (BankA[3] != ''):
                print("The Grass has been Eaten By The Cow")
                Lives = Lives - 1
            elif BankA[0] == '':
                print("the man and the boat are at the other end")
            else:
                BankB[0] = BankA[0]
                BankB[1] = BankA[1]
                BankA[0] = Boat
                BankA[1] = Boat
                print("The Tiger has been transferred from Bank A to Bank B")
        elif Choice == 6:
            if (BankB[2] != '') & (BankB[3] != ''):
                print("The Grass has been Eaten By The Cow")
                Lives = Lives - 1
            elif BankB[0] == '':
                print("the man and the boat are at the other end")
            else:
                BankA[0] = BankB[0]
                BankA[1] = BankB[1]
                BankB[0] = Boat
                BankB[1] = Boat
                print("The Tiger has been transferred from Bank B to Bank A")
        elif Choice == 7:
            if (BankB[2] != '') & (BankB[3] != ''):
                print("The Grass has been Eaten By The Cow")
                Lives = Lives - 1
            elif BankA[0] == '':
                print("the man and the boat are at the other end")
            else:
                BankB[0] = BankA[0]
                BankB[3] = BankA[3]
                BankA[0] = Boat
                BankA[3] = Boat
                print("The Grass has been transferred from Bank A to Bank B")
        elif Choice == 8:
            if (BankB[2] != '') & (BankB[3] != ''):
                print("The Grass has been Eaten By The Cow")
                Lives = Lives - 1
            elif BankB[0] == '':
                print("the man and the boat are at the other end")
            else:
                BankA[0] = BankB[0]
                BankA[3] = BankB[3]
                BankB[0] = Boat
                BankB[3] = Boat
                print("The Grass has been transferred from Bank B to Bank A")
        if Lives == 0:
            print("Game Over You Loose")
            break
    if BankA != ['','','','']:
        print("you have lost this game better luck next time")
    else:
        print("congratulations you have won this game")

while (1):
    BankA = ['Man,', 'Tiger,', 'Cow,', 'Grass,']
    BankB = ['', '', '', '']
    PlayC = input("Do You Want To Start A New Game ?")

    if PlayC.upper() == 'Y':
        PlayGame(BankA, BankB)
    else:
        print('bye')
        break
