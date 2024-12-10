#Using Dictionaries to make Tic-Tac-Toe(not complete)
theboard= {'L_TOP': ' ','M_TOP': ' ','R_TOP': ' ',
          'L_MID': ' ','M_MID': ' ','R_MID': ' ',
          'L_LOW': ' ','M_LOW': ' ','R_LOW': ' ',}

def printBoard(board):
    print(board['L_TOP'] + '|' + board['M_TOP'] + '|' + board['R_TOP'])
    print('-+-+-')
    print(board['L_MID'] + '|' + board['M_MID'] + '|' + board['R_MID'])
    print('-+-+-')
    print(board['L_LOW'] + '|' + board['M_LOW'] + '|' + board['R_LOW'])

turn = 'X'
for i in range(9):
    printBoard(theboard)
    print('Turn for ' + turn + '. Move on which space')
    move = input()
    theboard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
print(theboard)