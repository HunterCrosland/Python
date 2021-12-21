def createBoard():
    board = []
    for i in range(9):
        board.append([])
        for j in range(9):
            board[i].append(0)
    return board


dirMap = {"north": (0,1),
          "south": (0,-1),
          "east":  (-1,0),
          "west":  (1,0),
          "ne":    (1,1),
          "nw":    (-1,1),
          "se":    (1,-1),
          "sw":    (-1,-1)
}

def getColor(board,pos):
    try:
        return board[pos[0]][pos[1]]
    except:
        return None

def nextPos(pos,dir):
    return (pos[0] + dirMap[dir][0], pos[1] + dirMap[dir][1])

def isWinningPos(board,dir,currPos,color,num = 0):
    next = nextPos(currPos,dir)
    if num < 3:
        if getColor(board,next) == color:
            return isWinningPos(board,dir,next,color,num+1)
        else:
            return False
    else:
        return True

def recursePos(board,currPos,color):
    return (isWinningPos(board, "north",currPos,color) or 
            isWinningPos(board, "south",currPos,color) or
            isWinningPos(board, "east", currPos,color) or
            isWinningPos(board, "west", currPos,color) or
            isWinningPos(board, "ne",   currPos,color) or
            isWinningPos(board, "nw",   currPos,color) or
            isWinningPos(board, "se",   currPos,color) or
            isWinningPos(board, "sw",   currPos,color))

def makePlay(board,color,col):
    for i in range(8,-1,-1):
        if board[i][col] == 0:
            board[i][col] = color
            return (i,col)
        elif i == 0:
            return False

def printBoard(board):
    for row in board:
        print(row)

def playGame():
    board = createBoard()
    printBoard(board)
    winRed   = False
    winBlack = False

    while winRed == winBlack:
        a = False
        while a == False:
            redcol = int(input("Red Player: Input Column 1-9:"))
            a = makePlay(board,1,redcol-1)
            if a == False:
                print("Invalid input, try again.")

        printBoard(board)

        if recursePos(board, a, 1):
            winRed = True
            break

        b = False
        while b == False:
            blackcol = int(input("Black Player: Input Column 1-9:"))
            b = makePlay(board,2,blackcol-1)
            if b == False:
                print("Invalid input, try again.")

        printBoard(board)

        if recursePos(board, b, 2):
            winBlack = True
            break 

    if winRed:
        print("Congratulations Red, you win!")
    elif winBlack:
        print("Congratulations Black, you win!")
    else:
        print("It's a tie!")
    

def main():
    playGame()


main()
