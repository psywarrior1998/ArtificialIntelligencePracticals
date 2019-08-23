# Game of 8 puzzle without heuristic analysis it ends when it reaches local minima
import random

while True:
    ch = input("do you want to start the game?")
    if ch.lower() == 'y':
        puzzle = []
        for i in range(0, 3):
            puzzle.append([0, 0, 0])
        check = []
        for i in range(0, 9):
            while True:
                k = random.randint(1, 9)
                if k not in check:
                    check.append(k)
                    break
                else:
                    continue
        c = 0
        for i in range(0, 3):
            for j in range(0, 3):
                puzzle[i][j] = check[c]
                c = c + 1
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        h = 0
        ic = 0
        jc = 0
        ini = 0
        jni = 0
        cou = 0
        while puzzle != goal:
            for i in puzzle:
                print(i)
            hnew = 0
            for i in range(0, 3):
                for j in range(0, 3):
                    if puzzle[i][j] == goal[i][j]:
                        hnew = hnew + 1
            h = hnew
            print("your current heuristic score is " + str(h))
            choi = int(input("please choose the number you want to swap with 9"))
            if choi != 9:
                for i in range(0, 3):
                    for j in range(0, 3):
                        if puzzle[i][j] == choi:
                            ic = i
                            jc = j
                        elif puzzle[i][j] == 9:
                            ini = i
                            jni = j
                if ((ic + 1) == ini and jc == jni) or ((ic - 1) == ini and jc == jni) or (
                        ic == ini and (jc + 1) == jni) or (ic == ini and (jc - 1) == jni):
                    if puzzle[ic][jc] != goal[ic][jc]:
                        puzzle[ic][jc] = 9
                        puzzle[ini][jni] = choi
                        print("swapped")
                    else:
                        print("We cant move it as it will reduce the heuristic value")
                        cou = cou + 1
                else:
                    print("choose a value which has 9 as a neighbour")
            else:
                print("you cant choose 9 ")
            if cou == 4:
                print("Seems like you have reached your local minima")
                break
        print('congrats you have won the game !!!')
    elif ch.lower() == 'n':
        print("Bye Bye")
        break
