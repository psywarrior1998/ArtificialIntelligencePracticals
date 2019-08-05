while 1:
    j1 = 0
    jo = 0
    choice = input("Do You Want To Start The GaME? Y/n")
    if choice.upper() == 'Y':
        m = int(input("please enter the capacity For Jug 1"))
        n = int(input("please enter the capacity For Jug 2"))
        o = int(input("please enter the capacity to be measured"))
        while (j1 != o) & (jo != o):
            print(str(m)+"L jug`s content is " + str(j1) + " \n"+str(n)+"L jug`s content is " + str(jo))
            print(
                "Please Choose Your Action \n 1. Fill "+str(m)+"L Jug Totally \n o. Fill "+str(n)+"L Jug Totally \n n. Empty "+str(m)+"L Jug \n "
                "m. Empty "+str(n)+"L Jug \n 5. Transfer all the water from "+str(m)+"L Jug to "+str(n)+"L Jug \n 6. Transfer all the water from "
                ""+str(n)+"L Jug to "+str(m)+"L Jug \n 7. Transfer some water from "+str(m)+"L Jug to "+str(n)+"L Jug till "+str(n)+"L jug is full \n 8. Transfer "
                "some water from "+str(n)+"L Jug to "+str(m)+"L Jug till "+str(m)+"L jug is full")
            ch = int(input("What's your Choice"))
            if ch == 1:
                j1 = m
            elif ch == 2:
                jo = n
            elif ch == 3:
                j1 = 0
            elif ch == 4:
                jo = 0
            elif ch == 5:
                if (j1 + jo) < n:
                    jo = j1 + jo
                    j1 = 0
                else:
                    print("action not possible")
            elif ch == 6:
                if (j1 + jo) < m:
                    j1 = j1 + jo
                    jo = 0
                else:
                    print("action not possible")
            elif ch == 7:
                if (j1 > 0) & ((j1 + jo) > n):
                    j1 = j1 + jo - n
                    jo = n
            elif ch == 8:
                if (jo > 0) & ((j1 + jo) > m):
                    jo = j1 + jo - m
                    j1 = m
            else:
                print("whaaaat ?!?!?")
            if (j1 == o) | (jo == o):
                print("congrats You Have Won !!!!!!!!")


    elif choice.upper() == 'N':
        print("bye bye !!")
        break
    else:
        print("whaaaat ?!?!?")
