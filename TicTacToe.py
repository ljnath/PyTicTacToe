# Author : Lakhya Jyoti Nath (www.ljnath.com)
# Date : 30th Jan 2017
#
#A small Tic-Tac-Toe which i wrote while learing python
import os

"""
Main function for playing the game
"""
def playTicTacToe():
    gameplan = getGameplan()
    print("\nWelcome ", gameplan['p1Name'], "(", gameplan['p1Symbol'], ")", " and ",
          gameplan['p2Name'], "(", gameplan['p2Symbol'], ")", " to this game of Tic Tac Toe. Lets play")
    hasGameEnded = False
    isPlayer1CurrentPlayer = True
    isPlayer2CurrentPlayer = False
    currentPlayer = gameplan['p1Name']
    while hasGameEnded == False:
        gameplan = getUserInput(currentPlayer, gameplan)
        if isPlayer1CurrentPlayer:
            gameplan['board'][int(gameplan['p1Position'])
                              ] = gameplan['p1Symbol']
            drawBoard(gameplan['board'])
            hasGameEnded = checkGame(gameplan, currentPlayer)
            isPlayer1CurrentPlayer = False
            isPlayer2CurrentPlayer = True
            currentPlayer = gameplan['p2Name']
        elif isPlayer2CurrentPlayer:
            gameplan['board'][int(gameplan['p2Position'])
                              ] = gameplan['p2Symbol']
            drawBoard(gameplan['board'])
            hasGameEnded = checkGame(gameplan, currentPlayer)
            isPlayer1CurrentPlayer = True
            isPlayer2CurrentPlayer = False
            currentPlayer = gameplan['p1Name']


"""
Function for drawing the board after each input
"""
def drawBoard(board):
    os.system("cls")
    print("\nGame board : ")
    row = board
    print("\t        |       |       ")
    print("\t   ", row[0], "  |  ", row[1], "  |  ", row[2], "  ")
    print("\t -------|-------|-------")
    print("\t   ", row[3], "  |  ", row[4], "  |  ", row[5], "  ")
    print("\t -------|-------|-------")
    print("\t   ", row[6], "  |  ", row[7], "  |  ", row[8], "  ")
    print("\t        |       |\n")


"""
Function to check the game status
"""
def checkGame(gameplan, playerName):
    board = gameplan['board']

    if ((board[0] == board[1] == board[2] or
         board[0] == board[3] == board[6] or
         board[0] == board[4] == board[8]) and board[0] != ' '):
        print("Game Over! ", playerName, " is the winner")
        return True
    elif ((board[1] == board[4] == board[7] or
           board[3] == board[4] == board[5] or
           board[2] == board[4] == board[6]) and board[4] != ' '):
        print("Game Over! ", playerName, " is the winner")
        return True
    elif ((board[2] == board[5] == board[8] or
           board[6] == board[7] == board[8]) and board[8] != ' '):
        print("Game Over! ", playerName, " is the winner")
        return True
    elif gameplan['board'].count(' ') == 0:
        l1 = gameplan['board']
        l2 = gameplan['usedPosition']
        if l1.sort() == l2.sort():
            print("This game is  a tie!")
            return True
    else:
        return False


"""
Function to set the inital data for playing the game
"""
def getGameplan():
    l = [' '] * 9
    usedList = []
    gameplan = {"p1Name": "name", "p1Symbol": "X", "p1Position": "", "p2Name": "name","p2Symbol": "X", "p2Position": "", "board": l, "usedPosition": usedList}
    gameplan['p1Name'] = input("Player 1 - Enter your name : ")
    inputSymbol = 'A'
    while(inputSymbol != 'O' and inputSymbol != 'X'):
        inputSymbol = input(
            "Player 1 - Select your symbol (O or X) : ").upper()
    gameplan['p1Symbol'] = inputSymbol
    print("")
    gameplan['p2Name'] = input("Player 2 - Enter your name : ")
    if inputSymbol == 'O':
        gameplan['p2Symbol'] = 'X'
    else:
        gameplan['p2Symbol'] = 'O'
    return gameplan


"""
Function to get user inputs
"""
def getUserInput(playerName, gameplan):
    position = -1
    usedPosition = gameplan['usedPosition']
    while int(position) not in range(1, 10):
        position = input("Hi " + playerName +", enter your desired input position (1-9) : ")
        if int(position) not in range(1, 10):
            print("\nInvalid postion, position should be with 1 and 9")
        elif usedPosition.count(position) > 0:
            print("\nPosition already used !")
            position = -1
    gameplan['usedPosition'].append(position)
    position = int(position) - 1

    if(gameplan['p1Name'] == playerName):
        gameplan['p1Position'] = position
    else:
        gameplan['p2Position'] = position
    return gameplan


if __name__ == '__main__':
    playTicTacToe()
