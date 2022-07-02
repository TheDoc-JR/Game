from turtle import Screen, Turtle

scr = Screen()
scr.setup(1000, 1000)
scr.screensize(800, 800)

turt = Turtle()


def os(turt):
    return turt.circle(50)


def exes(turt):
    return turt.pendown(), turt.right(45), turt.forward(100), turt.left(135), \
           turt.penup(), turt.forward(75), turt.pendown(), turt.left(135), turt.forward(100)


def start(turt):
    return turt.penup(), turt.home()


def check(matrix, option):
    option = int(option)
    row = 0
    column = 0
    if option == 1:
        row = 0
        column = 0
    elif option == 2:
        row = 0
        column = 1
    elif option == 3:
        row = 0
        column = 2
    elif option == 4:
        row = 1
        column = 0
    elif option == 5:
        row = 1
        column = 1
    elif option == 6:
        row = 1
        column = 2
    elif option == 7:
        row = 2
        column = 0
    elif option == 8:
        row = 2
        column = 1
    elif option == 9:
        row = 2
        column = 2
    return matrix[row][column] != 0


def add(matrix, row, column, value):
    matrix[row][column] = value
    return matrix

def winnerO(matrix):
    if matrix[0][0] == 1 and matrix[0][1] == 1 and matrix[0][2] == 1:
        turt.backward(200)
        turt.left(90)
        turt.forward(30)
        turt.right(90)
        turt.pendown()
        turt.forward(400)
        start(turt)
        return True
    if matrix[1][0] == 1 and matrix[1][1] == 1 and matrix[1][2] == 1:
        turt.backward(200)
        turt.right(90)
        turt.forward(100)
        turt.left(90)
        turt.pendown()
        turt.forward(400)
        start(turt)
        return True
    if matrix[2][0] == 1 and matrix[2][1] == 1 and matrix[2][2] == 1:
        turt.backward(200)
        turt.right(90)
        turt.forward(225)
        turt.left(90)
        turt.pendown()
        turt.forward(400)
        start(turt)
        return True
    if matrix[0][0] == 1 and matrix[1][0] == 1 and matrix[2][0] == 1:
        turt.left(90)
        turt.forward(120)
        turt.left(90)
        turt.forward(130)
        turt.left(90)
        turt.pendown()
        turt.forward(420)
        start(turt)
        return True
    if matrix[0][1] == 1 and matrix[1][1] == 1 and matrix[2][1] == 1:
        turt.left(90)
        turt.forward(120)
        turt.left(180)
        turt.pendown()
        turt.forward(420)
        start(turt)
        return True
    if matrix[0][2] == 1 and matrix[1][2] == 1 and matrix[2][2] == 1:
        turt.left(90)
        turt.forward(120)
        turt.right(90)
        turt.forward(130)
        turt.right(90)
        turt.pendown()
        turt.forward(420)
        start(turt)
        return True
    if matrix[0][0] == 1 and matrix[1][1] == 1 and matrix[2][2] == 1:
        turt.left(90)
        turt.forward(100)
        turt.left(90)
        turt.forward(200)
        turt.left(135)
        turt.pendown()
        turt.forward(555)
        start(turt)
        return True
    if matrix[0][2] == 1 and matrix[1][1] == 1 and matrix[2][0] == 1:
        turt.left(90)
        turt.forward(100)
        turt.right(90)
        turt.forward(190)
        turt.right(135)
        turt.pendown()
        turt.forward(555)
        start(turt)
        return True

def winnerX(matrix):
    if matrix[0][0] == 2 and matrix[0][1] == 2 and matrix[0][2] == 2:
        turt.backward(200)
        turt.left(90)
        turt.forward(30)
        turt.right(90)
        turt.pendown()
        turt.forward(400)
        start(turt)
        return True
    if matrix[1][0] == 2 and matrix[1][1] == 2 and matrix[1][2] == 2:
        turt.backward(200)
        turt.right(90)
        turt.forward(100)
        turt.left(90)
        turt.pendown()
        turt.forward(400)
        start(turt)
        return True
    if matrix[2][0] == 2 and matrix[2][1] == 2 and matrix[2][2] == 2:
        turt.backward(200)
        turt.right(90)
        turt.forward(225)
        turt.left(90)
        turt.pendown()
        turt.forward(400)
        start(turt)
        return True
    if matrix[0][0] == 2 and matrix[1][0] == 2 and matrix[2][0] == 2:
        turt.left(90)
        turt.forward(120)
        turt.left(90)
        turt.forward(130)
        turt.left(90)
        turt.pendown()
        turt.forward(420)
        start(turt)
        return True
    if matrix[0][1] == 2 and matrix[1][1] == 2 and matrix[2][1] == 2:
        turt.left(90)
        turt.forward(120)
        turt.left(180)
        turt.pendown()
        turt.forward(420)
        start(turt)
        return True
    if matrix[0][2] == 2 and matrix[1][2] == 2 and matrix[2][2] == 2:
        turt.left(90)
        turt.forward(120)
        turt.right(90)
        turt.forward(130)
        turt.right(90)
        turt.pendown()
        turt.forward(420)
        start(turt)
        return True
    if matrix[0][0] == 2 and matrix[1][1] == 2 and matrix[2][2] == 2:
        turt.left(90)
        turt.forward(100)
        turt.left(90)
        turt.forward(200)
        turt.left(135)
        turt.pendown()
        turt.forward(555)
        start(turt)
        return True
    if matrix[0][2] == 2 and matrix[1][1] == 2 and matrix[2][0] == 2:
        turt.left(90)
        turt.forward(100)
        turt.right(90)
        turt.forward(190)
        turt.right(135)
        turt.pendown()
        turt.forward(555)
        start(turt)
        return True









turt.penup()
turt.forward(30)
turt.left(90)
turt.forward(100)
turt.left(90)
turt.forward(100)
turt.left(90)
turt.pendown()
turt.forward(390)
turt.penup()
turt.left(90)
turt.forward(130)
turt.pendown()
turt.left(90)
turt.forward(390)
turt.right(90)
turt.penup()
turt.forward(130)
turt.right(90)
turt.forward(130)
turt.right(90)
turt.pendown()
turt.forward(390)
turt.penup()
turt.left(90)
turt.forward(130)
turt.left(90)
turt.pendown()
turt.forward(390)

start(turt)

matrix = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]


roundsOs = 0
roundsXs = 0
rounds = 0

playerO = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

playerX = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

while rounds < 9 and not winnerO(matrix) and not winnerX(matrix):

    if roundsOs < 5 and not winnerO(matrix) and not winnerX(matrix):
        optionO = input('Please select an option to draw your O: ')
        while optionO not in '123456789':
            print(optionO + ' is not a valid option')
            optionO = input('Please select an option to draw your O: ')
        if optionO == '1':
            while check(matrix, optionO):
                print('This place is already taken')
                optionO = input('Please select an option to draw your O: ')
            else:
                if not check(matrix, optionO) and optionO == '1':
                    turt.backward(150)
                    turt.pendown()
                    os(turt)
                    start(turt)
                    add(matrix, 0, 0, 1)

        if optionO == '2':
            while check(matrix, optionO):
                print('This place is already taken')
                optionO = input('Please select an option to draw your O: ')
            else:
                if not check(matrix, optionO) and optionO == '2':
                    turt.backward(5)
                    turt.pendown()
                    os(turt)
                    start(turt)
                    add(matrix, 0, 1, 1)

        if optionO == '3':
            while check(matrix, optionO):
                print('This place is already taken')
                optionO = input('Please select an option to draw your O: ')
            else:
                if not check(matrix, optionO) and optionO == '3':
                    turt.forward(135)
                    turt.pendown()
                    os(turt)
                    start(turt)
                    add(matrix, 0, 2, 1)

        if optionO == '4':
            while check(matrix, optionO):
                print('This place is already taken')
                optionO = input('Please select an option to draw your O: ')
            else:
                if not check(matrix, optionO) and optionO == '4':
                    turt.backward(190)
                    turt.right(90)
                    turt.forward(95)
                    turt.pendown()
                    os(turt)
                    start(turt)
                    add(matrix, 1, 0, 1)

        if optionO == '5':
            while check(matrix, optionO):
                print('This place is already taken')
                optionO = input('Please select an option to draw your O: ')
            else:
                if not check(matrix, optionO) and optionO == '5':
                    turt.backward(55)
                    turt.right(90)
                    turt.forward(95)
                    turt.pendown()
                    os(turt)
                    start(turt)
                    add(matrix, 1, 1, 1)

        if optionO == '6':
            while check(matrix, optionO):
                print('This place is already taken')
                optionO = input('Please select an option to draw your O: ')
            else:
                if not check(matrix, optionO) and optionO == '6':
                    turt.forward(75)
                    turt.right(90)
                    turt.forward(95)
                    turt.pendown()
                    os(turt)
                    start(turt)
                    add(matrix, 1, 2, 1)

        if optionO == '7':
            while check(matrix, optionO):
                print('This place is already taken')
                optionO = input('Please select an option to draw your O: ')
            else:
                if not check(matrix, optionO) and optionO == '7':
                    turt.backward(190)
                    turt.right(90)
                    turt.forward(230)
                    turt.pendown()
                    os(turt)
                    start(turt)
                    add(matrix, 2, 0, 1)

        if optionO == '8':
            while check(matrix, optionO):
                print('This place is already taken')
                optionO = input('Please select an option to draw your O: ')
            else:
                if not check(matrix, optionO) and optionO == '8':
                    turt.backward(55)
                    turt.right(90)
                    turt.forward(230)
                    turt.pendown()
                    os(turt)
                    start(turt)
                    add(matrix, 2, 1, 1)

        if optionO == '9':
            while check(matrix, optionO):
                print('This place is already taken')
                optionO = input('Please select an option to draw your O: ')
            else:
                if not check(matrix, optionO) and optionO == '9':
                    turt.forward(75)
                    turt.right(90)
                    turt.forward(230)
                    turt.pendown()
                    os(turt)
                    start(turt)
                    add(matrix, 2, 2, 1)
        roundsOs += 1
    else:
        if winnerO(matrix):
            print('PLAYER 1 WON')
            break

    if roundsXs < 4 and not winnerO(matrix) and not winnerX(matrix):
        optionX = input('Please select an option to draw your X: ')
        while optionX not in '123456789':
            print(optionX + ' is not a valid option')
            optionX = input('Please select an option to draw your X: ')
        if optionX == '1':
            while check(matrix, optionX):
                print('This place is already taken')
                optionX = input('Please select an option to draw your X: ')
            else:
                if not check(matrix, optionX) and optionX == '1':
                    turt.backward(170)
                    turt.left(90)
                    exes(turt)
                    start(turt)
                    add(matrix, 0, 0, 2)

        if optionX == '2':
            while check(matrix, optionX):
                print('This place is already taken')
                optionX = input('Please select an option to draw your X: ')
            else:
                if not check(matrix, optionX) and optionX == '2':
                    turt.backward(35)
                    turt.left(90)
                    turt.forward(10)
                    exes(turt)
                    start(turt)
                    add(matrix, 0, 1, 2)

        if optionX == '3':
            while check(matrix, optionX):
                print('This place is already taken')
                optionX = input('Please select an option to draw your X: ')
            else:
                if not check(matrix, optionX) and optionX == '3':
                    turt.forward(95)
                    turt.left(90)
                    exes(turt)
                    start(turt)
                    add(matrix, 0, 2, 2)

        if optionX == '4':
            while check(matrix, optionX):
                print('This place is already taken')
                optionX = input('Please select an option to draw your X: ')
            else:
                if not check(matrix, optionX) and optionX == '4':
                    turt.backward(105)
                    turt.right(90)
                    turt.forward(60)
                    exes(turt)
                    start(turt)
                    add(matrix, 1, 0, 2)

        if optionX == '5':
            while check(matrix, optionX):
                print('This place is already taken')
                optionX = input('Please select an option to draw your X: ')
            else:
                if not check(matrix, optionX) and optionX == '5':
                    turt.forward(30)
                    turt.right(90)
                    turt.forward(65)
                    exes(turt)
                    start(turt)
                    add(matrix, 1, 1, 2)

        if optionX == '6':
            while check(matrix, optionX):
                print('This place is already taken')
                optionX = input('Please select an option to draw your X: ')
            else:
                if not check(matrix, optionX) and optionX == '6':
                    turt.forward(160)
                    turt.right(90)
                    turt.forward(65)
                    exes(turt)
                    start(turt)
                    add(matrix, 1, 2, 2)

        if optionX == '7':
            while check(matrix, optionX):
                print('This place is already taken')
                optionX = input('Please select an option to draw your X: ')
            else:
                if not check(matrix, optionX) and optionX == '7':
                    turt.backward(105)
                    turt.right(90)
                    turt.forward(200)
                    exes(turt)
                    start(turt)
                    add(matrix, 2, 0, 2)

        if optionX == '8':
            while check(matrix, optionX):
                print('This place is already taken')
                optionX = input('Please select an option to draw your X: ')
            else:
                if not check(matrix, optionX) and optionX == '8':
                    turt.forward(30)
                    turt.right(90)
                    turt.forward(200)
                    exes(turt)
                    start(turt)
                    add(matrix, 2, 1, 2)

        if optionX == '9':
            while check(matrix, optionX):
                print('This place is already taken')
                optionX = input('Please select an option to draw your X: ')
            else:
                if not check(matrix, optionX) and optionX == '9':
                    turt.forward(160)
                    turt.right(90)
                    turt.forward(200)
                    exes(turt)
                    start(turt)
                    add(matrix, 2, 2, 2)

        roundsXs += 1
    else:
        if winnerX(matrix):
            print('PLAYER 2 WON')
            break

    rounds = roundsOs + roundsXs
else:
    if rounds == 9:
        print('IT HAS BEEN A TIE!')

    elif winnerO(matrix):
        print('PLAYER 1 WON')

    elif winnerX(matrix):
        print('PLAYER 2 WON')





print(matrix)

scr.exitonclick()






