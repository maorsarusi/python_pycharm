import copy
from ex3_AI import alphaBetaPruning
import random

VICTORY = 10 ** 20  # The value of a winning board (for max)
LOSS = -VICTORY  # The value of a losing board (for max)
TIE = 0  # The value of a tie
SIZE = 4  # the length of winning seq.
COMPUTER = SIZE + 1  # Marks the computer's cells on the board
HUMAN = 1  # Marks the human's cells on the board

rows = 6
columns = 7
seq = 4


class game:
    board = []
    size = rows * columns
    playTurn = HUMAN

    # Used by alpha-beta pruning to allow pruning

    '''
    The state of the game is represented by a list of 4 items:
        0. The game board - a matrix (list of lists) of ints. Empty cells = 0,
        the comp's cells = COMPUTER and the human's = HUMAN
        1. The heuristic value of the state.
        2. Whose turn is it: HUMAN or COMPUTER
        3. Number of empty cells
    '''


def create(s):
    # Returns an empty board. The human plays first.
    # create the board
    s.board = []
    for i in range(rows):
        s.board = s.board + [columns * [0]]

    s.playTurn = HUMAN
    s.size = rows * columns
    s.val = 0.00001

    # return [board, 0.00001, playTurn, r*c]     # 0 is TIE


def cpy(s1):
    # construct a parent DataFrame instance
    s2 = game()
    s2.playTurn = s1.playTurn
    s2.size = s1.size
    s2.board = copy.deepcopy(s1.board)
    #      print("board ", s2.board)
    return s2


def value1(s):
    # Returns the heuristic value of s
    if random.random() > 0.1:
        return random.random() * 10
    else:
        return random.choice([LOSS, VICTORY, TIE])


def value(s):
    # Returns the heuristic value of s, and gives value according to the length
    height = checkHeight(s)  # find sequence in height
    line = checkLine(s)  # find sequence in line
    left = checkLeftDiagonal(s)  # find sequence in left diagonal
    right = checkRightDiogonal(s)  # find sequence in right diagonal

    if 4 in [height, line, left, right]:
        # check if there is connect 4
        if s.playTurn == HUMAN:
            return VICTORY
        else:
            return LOSS
    if 3 in [height, line, left, right]:
        # check if there is connect 3
        if s.playTurn == HUMAN:
            return 10 ** 19
        else:
            return -10 ** 18
    if 2.5 in [height, line, left, right]:
        # check if there is a back threat
        if s.playTurn == COMPUTER:
            return 10 ** 17
        else:
            return -10 ** 16
    if 2 in [height, line, left, right]:
        if s.playTurn == COMPUTER:
            return 10 ** 15
        else:
            return -10 ** 14
    if 1 in [height, line, left, right]:
        # check if there is connect 2
        if s.playTurn == COMPUTER:
            return 10 ** 2
        else:
            return -10
    if 0 in [height, line, left, right]:
        # Checks whether there is a move that could lead to Sequence 4
        if s.playTurn == COMPUTER:
            return -100
        else:
            return 100
    if -1 in [height, line, left, right] or s.size == 0:
        return TIE


def bTLine(s):
    # this case happend for each i
    # and for each j between 1-5

    for i in range(5, -1, -1):
        for j in range(1, 4):
            if not s.board[i][j] == 0:
                if s.board[i][j] == s.board[i][j + 2]:
                    if s.board[i][j + 1] == 0:
                        return True
                elif s.board[i][j] == s.board[i][j + 1]:
                    if s.board[i][j - 1] == 0 and s.board[i][j + 2] == 0:
                        return True
    return False


def bTHeigtRDiagonal(
        s):  # this is a back trapping case for right diagonal and line (we try to get it put its coin in the height so we will win at the diagonal)
    # this case happend for i between 2-3
    # and j between 0-3
    for i in range(3, 1, -1):
        for j in range(0, 4):
            if not s.board[i][j] == 0:
                if s.board[i + 1][j] == s.board[i + 2][j] and s.board[i + 1][j] == s.board[i - 1][j + 1] and \
                        s.board[i - 1][j] == s.board[i][j + 2] and s.board[i - 1][j] == s.board[i + 1][j + 3]:
                    return True
    return False


def bTHeigtLDiagonal(
        s):  # this is a back trapping case for  leftdiagonal and line (we try to get it put its coin in the height so we will win at the diagonal)
    # this case happend for each i between 2-3
    # and j between 3-6
    for i in range(3, 1, 1):
        for j in range(3, 7):
            if not s.board[i][j] == 0:
                if s.board[i + 1][j] == s.board[i + 2][j] and s.board[i - 1][j - 1] == s.board[i + 1][j] and s.board[i][
                    j - 2] and s.board[i + 1][j] == s.board[i + 1][j - 3]:
                    return True

    return False


def checkHeight(s, num=4):
    # recursive func the find sequence in columns and return the length of the seq
    if num == 0:
        return num
    for i in range(5, rows - 4, -1):  # loop runing from 5 to the max row that enable the required sequence
        for j in range(0, columns):  # loop runing from 0 - columns (CONST)
            human = 0
            comp = 0
            zero = 0
            for k in range(i, i - 4, -1):  # loop runing several times according to the required sequence
                if s.board[k][j] == HUMAN:
                    human += 1
                if s.board[k][j] == COMPUTER:
                    comp += 1
                if s.board[k][j] == 0:
                    zero += 1
                if (num + zero == 4) and (human == 0 or comp == 0) and (num in [human, comp]):
                    return num
    return checkHeight(s, (
                num - 1))  # If the current sequence is not found, recursively sends a lower sequence to search recursively sends a lower sequence to search


def checkLine(s, num=4):  # def checkLine(s,num = 3): # to rate diferent level for each line
    # recursive func the find sequence in rows and return the length of the seq
    if num == -1:
        return num
    if num == 2 and bTLine(s):  # analize if there is a"back threat" and return appropriate value
        return 1.5
    for i in range(0, rows):  # loop runing from 0 - rows (CONST)
        for j in range(0, columns - 3):  # loop runing from 0 to the max columns that enable the required sequence
            # if not s.board[i][j] == 0:
            # count = 0
            # zero = 0
            human = 0
            comp = 0
            for k in range(j, j + 4):  # loop runing several times according to the required sequence
                if s.board[i][k] == HUMAN:
                    human += 1
                if s.board[i][k] == COMPUTER:
                    comp += 1
            if (human == 0 or comp == 0) and (num in [human, comp]):
                return num
    return checkLine(s, (num - 1))  # If the current sequence is not found,
    # recursively sends a lower sequence to search


def checkRightDiogonal(s, num=4):
    # recursive func the find sequence in left diagonal and return the length of the seq
    if num == -1:
        return num
    if num == 2 and bTHeigtRDiagonal(s):  # analize if there is a"back threat" and return appropriate value
        return 1.5
    for i in range(0, rows - 3):  # loop runing from 0 to the max rows that enable the required sequence in diagonal
        for j in range(0,
                       columns - 3):  # loop runing from 0 to the max columns that enable the required sequence in diagonal
            human = 0
            comp = 0
            for r, c in zip(range(i, i + 4),
                            range(j, j + 4)):  # loop runing several times according to the required sequence
                if (not c == j + 3) and (r < 4 and c < 6) and (
                        s.board[r + 2][c + 1] == 0):  # Checks whether diagonal continuation is possible
                    human = comp = 1
                    break
                if s.board[r][c] == HUMAN:
                    human += 1
                if s.board[r][c] == COMPUTER:
                    comp += 1
            if (human == 0 or comp == 0) and (num in [human, comp]):
                return num
    return checkRightDiogonal(s, (num - 1))  # If the current sequence is not found,
    # recursively sends a lower sequence to search


def checkLeftDiagonal(s, num=4):
    # recursive func the find sequence in right diagonal and return the length of the seq
    if num == -1:
        return num
    if num == 2 and bTHeigtLDiagonal(s):
        return 1.5
    for i in range(3, rows):  # loop runing from 3 to the max rows that enable the required sequence in diagonal
        for j in range(0,
                       columns - 3):  # loop runing from 0 to the max columns that enable the required sequence in diagonal
            human = 0
            comp = 0
            for r, c in zip(range(i, i - 4, -1),
                            range(j, j + 4)):  # loop runing several times according to the required sequence
                if (not c == j + 3) and (c < 6) and (
                        s.board[r][c + 1] == 0):  # Checks whether diagonal continuation is possible
                    human = comp = 1
                    break
                if s.board[r][c] == HUMAN:
                    human += 1
                if s.board[r][c] == COMPUTER:
                    comp += 1
            if (human == 0 or comp == 0) and (num in [human, comp]):
                return num
    return checkLeftDiagonal(s, (num - 1))  # If the current sequence is not found,
    # recursively sends a lower sequence to search


def printState(s):
    # Prints the board. The empty cells are printed as numbers = the cells name(for input)
    # If the game ended prints who won.
    for r in range(rows):
        print("\n|", end="")
        # print("\n",len(s[0][0])*" --","\n|",sep="", end="")
        for c in range(columns):
            if s.board[r][c] == COMPUTER:
                print("X|", end="")
            elif s.board[r][c] == HUMAN:
                print("O|", end="")
            else:
                print(" |", end="")

    print()

    for i in range(columns):
        print(" ", i, sep="", end="")

    print()

    val = value(s)

    if val == VICTORY:
        print("I won!")
    elif val == LOSS:
        print("You beat me!")
    elif val == TIE:
        print("It's a TIE")


def isFinished(s):
    # Seturns True iff the game ended
    return value(s) in [LOSS, VICTORY, TIE] or s.size == 0


def isHumTurn(s):
    # Returns True iff it is the human's turn to play
    return s.playTurn == HUMAN


def decideWhoIsFirst(s):
    # The user decides who plays first
    if int(input("Who plays first? 1-me / anything else-you : ")) == 1:
        s.playTurn = COMPUTER
    else:
        s.playTurn = HUMAN

    return s.playTurn


def makeMove(s, c):
    # Puts mark (for huma. or comp.) in col. c
    # and switches turns.
    # Assumes the move is legal.

    r = 0
    while r < rows and s.board[r][c] == 0:
        r += 1

    s.board[r - 1][c] = s.playTurn  # marks the board
    s.size -= 1  # one less empty cell
    if (s.playTurn == COMPUTER):
        s.playTurn = HUMAN
    else:
        s.playTurn = COMPUTER


def inputMove(s):
    # Reads, enforces legality and executes the user's move.

    # self.printState()
    flag = True
    while flag:
        c = int(input("Enter your next move: "))
        if c < 0 or c >= columns or s.board[0][c] != 0:
            print("Illegal move.")
        else:
            flag = False
            makeMove(s, c)


def getNext(s):
    # returns a list of the next states of s
    ns = []
    for c in list(range(columns)):
        #   print("c=",c)
        if s.board[0][c] == 0:
            #    print("possible move ", c)
            tmp = cpy(s)
            makeMove(tmp, c)
            #    print("tmp board=",tmp.board)
            ns += [tmp]
        #    print("ns=",ns)
    #  print("returns ns ", ns)
    return ns


def inputComputer(s):
    return alphaBetaPruning.go(s)
