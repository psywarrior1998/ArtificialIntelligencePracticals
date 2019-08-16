#this the 4 queen problem game 
while 1:
    queen = 4
    board = [['A', 'A', 'A', 'A'], ['A', 'A', 'A', 'A'], ['A', 'A', 'A', 'A'], ['A', 'A', 'A', 'A']]
    ch = input("Wanna Start The Game ?")
    if ch.lower() == 'y':
        row = queen
        a = []
        ab=[]
        for i in range(0, queen):
            a = a + ['A']
        for i in range(0,queen):
            ab = ab + [a]
        for i in ab:
            print(i)
        while row != 0:
            print("---------------")
            for i in board:
                print(i)
            print(str(row) + " queens are still left to be placed by you ")
            qp = int(
                input("Please choose the position from in which you wanna place the queen in row " + str(
                    queen - row + 1)))
            if board[queen - row][qp - 1] != 'B':
                a = ['B', 'B', 'B', 'B']
                a[qp - 1] = 'Q'
                board[queen - row] = a
                for i in range((queen - row + 1), queen):
                    board[i][qp - 1] = 'B'
                    if (qp + (i - queen + row) - 1) < 4:
                        board[i][qp + (i - queen + row) - 1] = 'B'
                    if 0 <= (qp - (i - queen + row) - 1):
                        print(str(qp - (i - queen + row - 1)))
                        board[i][qp - (i - queen + row) - 1] = 'B'
                for i in board:
                    print(i)

                row = row - 1
            else:
                print("this position is already blocked \n 'GaMe OvEr'")
                break
        count = 0
        for i in board:
            for j in i:
                if j == 'A':
                    count += 1
        if count == 0:
            print("Congratulations you have won the game !!!")
    elif ch.lower() == 'n':
        print("Bye Bye !!!")
        break
    else:
        print("Whaaaaaaaaaaat?!?!?!?!?!?!?!?!?!")
