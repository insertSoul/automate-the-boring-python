# Aim of program is to check if a chess board is valid

# for a chess board to be valid it must:
    # have exactly 1 black king 'bking' and one white king 'wking' [kingCheck]
    # no more than 16 pieces total (per side) [pieceCountCheck]
    # no more than 8 pawns (bpawn/wpawn) [pawnCheck]
    # sit on a valid space ('1a' to '8h') (nested loops?) [positionCheck]
    # names begin with w or b AND only followed by 'pawn', 'kinght', 'bishop', 'rook', 'queen' or king'. [pieceCheck]

# create dictionary of chess pieces
import time


currentBoard = {'1h': 'bking', '6c': 'wqueen', '8g': 'bbishop', '5h': 'bqueen', '3e': 'wking',}

falseBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
                '5h': 'bqueen', '3e': 'wking' , '2e': 'bking',
                '6h': 'bpawn', '3b': 'bpawn' , '4c': 'bpawn', '7e': 'wpawn',
                '2a' : 'wpawn'}

falseBoard1 = { '9h' : 'bking' }

falseBoard2 = { '2a' : 'bpawn' , '2b' : 'bpawn' , '2c' : 'bpawn' , '2d' : 'bpawn' , '2e' : 'bpawn' ,
                '2f' : 'bpawn' , '2g' : 'bpawn' , '2h' : 'bpawn'  }


def isValidChessBoard(board):
    #set all checks to false
    kingCheck = False
    pieceCountCheck = False
    pawnCheck = False
    positionCheck = False
    pieceCheck = False

    # kingCheck
    pieceList = (list(board.values())) # create a list to count pieces
    if pieceList.count('bking') == 1:
        if pieceList.count('wking') == 1: # if there are exactly 1 of each
            print('King check complete')
            kingCheck = True # set the check to truw
        else:
            print ('King check Failed')
    else:
        print ('King check Failed')


    # pieceCountCheck
    blackPiece = 0
    whitePiece = 0
    for i in range(len(pieceList)): # go through the created list
        pieceChecks = str(pieceList[i])  # take each piece from list
        if pieceChecks[0] == 'b': # check if theres a b at start and add 1 to counter
            blackPiece += 1
        if pieceChecks[0] == 'w': # check if theres a w  at start and add 1 to counter
            whitePiece += 1
    if blackPiece <= 16 and whitePiece <= 16: # if both are 16 or under set to true
        print('Piece count complete')
        pieceCountCheck = True
    else:
        print ('Piece count failed')

    #pawnCheck
    if (pieceList.count('bpawn')) <= 8 and (pieceList.count('wpawn')) <=8: # count instances of both lists and if over 8 false
        print('Pawn check complete')
        pawnCheck = True
    else:
         print('Pawn check failed')

    #positionCheck
    validLetters = ('a','b','c','d','e','f','g','h')
    positionChecksCount = 0
    for i in board.keys(): # loop through keys (positions)
        if int(i[0]) <= 8 and i[1] in validLetters: #if 1st digit is 8 or less AND 2nd is a-h add to counter
            positionChecksCount += 1
    if positionChecksCount == len(board.keys()): # if all where valid it is true
        print('Position check complete')
        positionCheck = True
    else:
        print('Position check failed')

    #pieceCheck
    correctPositionCount = 0
    for i in (list(currentBoard.values())):
        if str(i[0]) == 'w' or 'b':
            if str(i[1:-1]) == 'pawn' or 'kinght' or 'bishop' or 'rook' or 'queen' or 'king':
                correctPositionCount += 1
    if correctPositionCount == len(currentBoard):
        print('Piece check complete')
    else:
        print('Piece check failed')

    if  kingCheck == True and pieceCountCheck == True and pawnCheck == True and positionCheck == True:
        time.sleep(1)
        print()
        print('all checks complete....')
        time.sleep(0.8)
        print('This is a valid chess board')
    else:
            time.sleep(1)
            print()
            print('all checks complete....')
            time.sleep(0.8)
            print('One or more checks have failed, this is not a valid chess board')


 # Tests
# function call
isValidChessBoard(currentBoard)
# isValidChessBoard(falseBoard)
#isValidChessBoard(falseBoard1)
isValidChessBoard(falseBoard2)
