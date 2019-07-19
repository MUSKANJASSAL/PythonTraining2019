# 8 X 8 Chess Board
import numpy as np
x = np.ones((3,3))
print("Checkerboard pattern:")
chessBoard = np.zeros((8,8), dtype=int)
chessBoard[1::2,::2] = 1
chessBoard[::2,1::2] = 1
print(chessBoard)

# 2. Ask User to Place 4 queens on ChessBoard
# Where to place 1st Queen: 2,3
# Where to place 2nd Queen: 1,4
# Where to place 3rd Queen: 5,6
# Where to place 4th Queen: 7,7
# And substitute 9 over there !!

queenPosition = input("Where to place 1st Queen:")
i = int(queenPosition[0])
j = int(queenPosition[2])
chessBoard[i][j] = 9
print(chessBoard)
# second()
# third()

# Validate if a Queen is available in the same row or same column
# Give a message to User to enter some diiferent position

"""
def second():
    secondqueenPosition = input("Where to place 2nd Queen:")
    if queenPosition != secondqueenPosition:
        i = int(secondqueenPosition[0])
        j = int(secondqueenPosition[2])
        chessBoard[i][j] = 9
        print(chessBoard)
        return(secondqueenPosition)
    else:
        print("Not Valid !!")
        print("Try again")
        second()

def third():
    thirdqueenPosition = input("Where to place 3rd Queen:")
    if queenPosition and secondqueenPosition != thirdqueenPosition:
        i = int(thirdqueenPosition[0])
        j = int(thirdqueenPosition[2])
        chessBoard[i][j] = 9
        print(chessBoard)
    else:
        print("Not Valid !!")
        print("Try again")
        third()

queenPosition = input("Where to place 1st Queen:")
i = int(queenPosition[0])
j = int(queenPosition[2])
chessBoard[i][j] = 9
print(chessBoard)
second()
third()
"""
indexes = []

for i in range(0,4):
    queenPosition = input("Enter the position where you want to enter #{}". format(i))
    i = chessBoard[0]
    j = chessBoard[2]

    if i not in indexes and j not in

# Validate if a Queen is available in the same diagonal
# Give a message to User to enter some diiferent position
