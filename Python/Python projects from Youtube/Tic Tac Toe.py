board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

currentPlayer = "X"
winner = None
gameRunning = True

#printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("_________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("_________")
    print(board[6] + " | " + board[7] + " | " + board[8])
print(printBoard(board))

#take player input 
def playerInput(board):
    inp = int(input("Enter a number from 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "_":
        board[inp - 1] = currentPlayer 
    else:
        print("This place is already taken! Enter another one")

#check for win or tie
def checkH(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != '_':
        winner = board[4]
        return True
    elif board[6] == board[7] == board[8] and board[7] != '_':
        winner = board[7]
        return True
        

def checkV(board):
    global winner
    if board[0] == board[3] == board[5] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        return True
        
        
def checkD(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True
        
        
def checkTie(board):
    global gameRunning
    if "_" not in board:
        print("It is a tie!")
    gameRunning = False

def checkWin(board):
    global gameRunning
    if checkH(board) == True  or checkV(board) == True  or checkD(board) == True :
        print(f"The winner is {winner}")
        print(printBoard(board))
        gameRunning = False




#switch player
def switch():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"




while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    switch()