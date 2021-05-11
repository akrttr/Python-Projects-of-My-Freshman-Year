def SetTable(table, size):
    for i in range(size):
        for j in range(size):
            print("%4s" % (table[i][j]), end="")
        print()


table = []

size = int(input("Enter the Game Board Size:"))

for i in range(size):
    table.append([])
    for j in range(size):
        table[i].append(i * size + j)

SetTable(table, size)


def p1choose():
    k = int(input("Player 1 turn -->"))
    row = k // size
    column = k % size
    if table[row][column] == k:
        table[row][column] = "X"
        SetTable(table, size)
    elif table[row][column] == "O":
        print("The other player select this cell before.")
    else:
        print("You have made this choice before.")
    winninghorizontal()
    winningcrosswise()
    p2choose()


def p2choose():
    k = int(input("Player 2 turn -->"))
    row = k // size
    column = k % size
    if table[row][column] == k:
        table[row][column] = "O"
        SetTable(table, size)
    elif table[row][column] == "X":
        print("The other player selected this cell before.")
    else:
        print("You have made this choice before.")
    winninghorizontal()
    winningcrosswise()
    p1choose()


def winninghorizontal():
    for i in range(size):
        for j in range(size):
            xnumb = table[i].count("X")
            if xnumb == size:
                print("winner is player 1")
                exit()
    for i in range(size):
        for j in range(size):
            xnumb = table[i].count("O")
            if xnumb == size:
                print("winner is player 2")
                exit()


"""def winningvertical():
    for i in range(size):
        for j in range(size):
            table[i][j] == "X"
"""

def winningcrosswise():
    counter = 0
    for i in range(size):
        for j in range(size):
            if i == j and table[i][j] == "X":
                counter += 1
                if counter == size:
                    print("Winner is player 1")
                    exit()
    counter2 = 0
    for i in range(size):
        for j in range(size):
            if i == j and table[i][j] == "O":
                counter2 += 1
                if counter2 == size:
                    print("Winner is player 2")
                    exit()


while size > 0:
    p1choose()
    p2choose()
else:
    print("Enter a positive value!")
