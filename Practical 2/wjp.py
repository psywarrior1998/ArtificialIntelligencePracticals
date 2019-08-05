while 1:
    j1 = 0
    j2 = 0
    choice = input("Do You Want To Start The GaME? Y/n")
    if choice.upper() == 'Y':
        while (j1 != 2) & (j2 != 2):
            print("4L jug`s content is " + str(j1) + " \n3L jug`s content is " + str(j2))
            print(
                "Please Choose Your Action \n 1. Fill 4L Jug Totally \n 2. Fill 3L Jug Totally \n 3. Empty 4L Jug \n "
                "4. Empty 3L Jug \n 5. Transfer all the water from 4L Jug to 3L Jug \n 6. Transfer all the water from "
                "3L Jug to 4L Jug \n 7. Transfer some water from 4L Jug to 3l Jug till 3L jug is full \n 8. Transfer "
                "some water from 3L Jug to 4L Jug till 4L jug is full")
            ch = int(input("What's your Choice"))
            if ch == 1:
                j1 = 4
            elif ch == 2:
                j2 = 3
            elif ch == 3:
                j1 = 0
            elif ch == 4:
                j2 = 0
            elif ch == 5:
                if (j1 + j2) < 3:
                    j2 = j1 + j2
                    j1 = 0
                else:
                    print("action not possible")
            elif ch == 6:
                if (j1 + j2) < 4:
                    j1 = j1 + j2
                    j2 = 0
                else:
                    print("action not possible")
            elif ch == 7:
                if (j1 > 0) & ((j1 + j2) > 3):
                    j1 = j1 + j2 - 3
                    j2 = 3
            elif ch == 8:
                if (j2 > 0) & ((j1 + j2) > 4):
                    j2 = j1 + j2 - 4
                    j1 = 4
            else:
                print("whaaaat ?!?!?")
            if (j1 == 2) | (j2 == 2):
                print("congrats You Have Won !!!!!!!!")


    elif choice.upper() == 'N':
        print("bye bye !!")
        break
    else:
        print("whaaaat ?!?!?")
