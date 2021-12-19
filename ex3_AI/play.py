# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:15:37 2020o1


@author: צור איתן לוי מאור סרוסי
"""

from ex3_AI import game

board = game.game()
game.create(board)
print("Initial Game")
game.printState(board)
game.decideWhoIsFirst(board)
while not game.isFinished(board):
    print("continue game")
    if game.isHumTurn(board):
        game.inputMove(board)
    else:
        #  board=game.inputComputer(board)

        game.inputMove(board)
    game.printState(board)

print("Game Over:")
