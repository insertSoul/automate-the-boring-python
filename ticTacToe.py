# a blank board
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' ',}

# a filled in board

# theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M':
# 'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

validInputs = ["top-L" , "top-M" , "top-R" , "mid-L" , "mid-M" , "mid-R" , "low-L" , "low-M" , "low-R"]
turnCounter = 9

print("To input in a space use top- mid- or low- followed by L M or R")
print("E.g Top-L for top left or Mid-M for the center")
turn = 'X'
while turnCounter > 0:
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    if move in validInputs:
        turnCounter -= 1
        theBoard[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    else:
        print("That is not a valid move, Please try again")
printBoard(theBoard)
