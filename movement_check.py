def checking_row(r):
    player = sum(1 for i in r if i == 'X')
    ai = sum(1 for i in r if i == 'O')
    return player, ai
def checking_column(rows, n):
    r1,r2,r3=rows
    col = [r1[n], r2[n], r3[n]]
    player = sum(1 for i in col if i == 'X')
    ai = sum(1 for i in col if i == 'O')
    return player, ai
def checking_diagonal1(rows):
    r1,r2,r3=rows
    diag = [r1[0], r2[1], r3[2]]
    player = sum(1 for i in diag if i == 'X')
    ai = sum(1 for i in diag if i == 'O')
    return player, ai

def checking_diagonal2(rows):
    r1,r2,r3=rows
    diag = [r1[2], r2[1], r3[0]]
    player = sum(1 for i in diag if i == 'X')
    ai = sum(1 for i in diag if i == 'O')
    return player, ai
def check_if_movement_is_possible(r):
    for i,val in enumerate(r):
        if val == ' ':
            return i
    else:
        return False
def board_full(rows):
    r1,r2,r3=rows
    return all(cell != ' ' for row in (r1, r2, r3) for cell in row)
def winner(rows):
    # row
    r1,r2,r3=rows
    for r in (r1, r2, r3):
        if r == ['X','X','X']: return 'X'
        if r == ['O','O','O']: return 'O'
    # column
    for c in range(3):
        col = [r1[c], r2[c], r3[c]]
        if col == ['X','X','X']: return 'X'
        if col == ['O','O','O']: return 'O'
    # diagonal
    d1 = [r1[0], r2[1], r3[2]]
    d2 = [r1[2], r2[1], r3[0]]
    if d1 == ['X','X','X'] or d2 == ['X','X','X']: return 'X'
    if d1 == ['O','O','O'] or d2 == ['O','O','O']: return 'O'
    return None
def wincheck(rows):

    if (winner(rows) == 'X'):
        print('X wins!')
    elif (winner(rows) == 'O'):
        print('O wins!')
    elif (winner(rows) == None and board_full(rows)):
        print('Draw')
    else:
        pass