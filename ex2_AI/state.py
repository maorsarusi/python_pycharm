'''
The state is a list of 2 items: the board, the path
The target for 8-puzzle is: (zero is the hole)
012
345
678
'''

import random
import math


# returns a random board nXn
def create(n):
    s = list(range(n * n))  # s is the board itself. a vector that represent a matrix. s=[0,1,2....n^2-1]
    m = "<>v^"  # m is "<>v^" - for every possible move (left, right, down, up)
    for i in range(n * n * n):  # makes n^3 random moves
        if_legal(s, m[random.randrange(4)])
    return [s, ""]  # at the beginning "" is an empty path, later on path
    # contains the path that leads from the initial state to the state


def get_next(x):  # returns a list of the children states of x
    ns = []  # the next state list
    for i in "<>v^":
        s = x[0][:]  # [:] - copies the board in x[0]
        if_legal(s, i)  # try to move in direction i
        # checks if the move was legal and...
        if s.index(0) != x[0].index(0) and \
                (x[1] == "" or x[1][-1] != "><^v"[
                    "<>v^".index(i)]):  # check if it's the first move or it's a reverse move
            ns.append([s, x[1] + i])  # appends the new state to ns
    return ns


def path_len(x):
    return len(x[1])


def is_target(x):
    n = len(x[0])  # the size of the board
    return x[0] == list(range(n))  # list(range(n)) is the target state


#############################
def if_legal(x, m):  # gets a board and a move and makes the move if it's legal
    n = int(math.sqrt(len(x)))  # the size of the board is nXn
    z = x.index(0)  # z is the place of the empty tile (0)
    if z % n > 0 and m == "<":  # checks if the empty tile is not in the first col and the move is to the left
        x[z] = x[z - 1]  # swap x[z] and x[z-1]...
        x[z - 1] = 0  # ...and move the empty tile to the left
    elif z % n < n - 1 and m == ">":  # check if the empty tile is not in the n's col and the move is to the right
        x[z] = x[z + 1]
        x[z + 1] = 0
    elif z >= n and m == "^":  # check if the empty tile is not in the first row and the move is up
        x[z] = x[z - n]
        x[z - n] = 0
    elif z < n * n - n and m == "v":  # check if the empty tile is not in the n's row and the move is down
        x[z] = x[z + n]
        x[z + n] = 0


def hdistance(s):  # the heuristic value of s
    return hdistance1(s)  # What kind of search is this??? g


# זה התשובה לשאלה 3
def hdistance1(s):
    count = 0
    for i in range(0, len(s[0])):  # runnig on the list that the puzzle is in it
        if not i == s[0][i]:  # checking if the number isn't in its place
            count += 1
    return count  # Returns the number of the misplaced tiles


# תשובה לשאלה 4:כמובן שעבור n=3 זה יפעל אך השינוי הוא שזה גם מידי פעם(אמנם לא ביעילות)
# עובד עבור n=4 כמו"כ נשים לב שמספר בדיקות המצבים שנותרו ומספר המצבים שלא נבדקו קטן בהרבה (מכיוון שמס' המצבים קטן)

# שאלה 5
def hdistance2(s):
    count = 0  # this is the counter for menhaten distance
    length = math.sqrt(len(s[0]))  # this is for the sqrt that we divideing

    for i, item in enumerate(s[0]):  # we running at the place and the item in s[0]
        if not item == 0:  # don't calculate the distance of 0 from the void place
            x_goal, y_goal = int(item / length), int(item % length)  # the place that the number need to be

            x_place, y_place = int(i / length), int(i % length)  # the aqual place of the number

            count += (abs(x_goal - x_place) + abs(
                y_goal - y_place))  # we need to substract the actul place and the goal place

    return count

# שאלה 6
# כמובן שגם פה יש הבדל מהותי בין הרצה של  n=3  ו n=4
# אך יןתר מעניין ההבדל בין שתי היוריסטיקות 
# בשאלה 3יש לא יותר מצבים ומטבע הדברים הוא בודק יותר(לכן זה איטי יותר)
# לעומת זאת בשאלה 5 יש הרבה פחות מצבים ומטבע הדברים פחות בדיקות ולכן זה מהיר יותר
