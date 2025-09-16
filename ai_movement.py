import movement_check
def ai_move(rows):
    #ai win-check
    # ai check win move for diagonals
    player, ai = movement_check.checking_diagonal1(rows)
    if ai == 2:
        for k in range(3):
            if rows[k][k] == ' ':
                rows[k][k] = 'O'
                return rows

    player, ai = movement_check.checking_diagonal2(rows)
    if ai == 2:
        diag = [(0, 2), (1, 1), (2, 0)]
        for r, c in diag:
            if rows[r][c] == ' ':
                rows[r][c] = 'O'
                return rows
    #ai check win move for rows
    for row in rows:
        player, ai = movement_check.checking_row(row)
        idx = movement_check.check_if_movement_is_possible(row)
        if ai == 2 and idx is not False:
            row[idx] = 'O'
            return rows
    #ai check win move for columns
    for c in range(3):
        player, ai = movement_check.checking_column(rows, c)
        if ai == 2:
            for r in range(3):
                if rows[r][c] == ' ':
                    rows[r][c] = 'O'
                    return rows
    #ai player-defense
    # ai check defense move for diagonals
    player, ai = movement_check.checking_diagonal1(rows)
    if player == 2:
        for k in range(3):
            if rows[k][k] == ' ':
                rows[k][k] = 'O'
                return rows

    player, ai = movement_check.checking_diagonal2(rows)
    if player == 2:
        diag = [(0, 2), (1, 1), (2, 0)]
        for r, c in diag:
            if rows[r][c] == ' ':
                rows[r][c] = 'O'
                return rows
    #ai check defense move for rows
    for row in rows:
        player, ai = movement_check.checking_row(row)
        idx = movement_check.check_if_movement_is_possible(row)
        if player == 2 and idx is not False:
            row[idx] = 'O'
            return rows
    #ai check defense move for columns
    for c in range(3):
        player, ai = movement_check.checking_column(rows, c)
        if ai == 2:
            for r in range(3):
                if rows[r][c] == ' ':
                    rows[r][c] = 'O'
                    return rows
    #ai normal attacking moveset
    # ai check attacking move for diagonals
    player, ai = movement_check.checking_diagonal1(rows)
    if ai == 1:
        for k in range(3):
            if rows[k][k] == ' ':
                rows[k][k] = 'O'
                return rows

    player, ai = movement_check.checking_diagonal2(rows)
    if ai == 1:
        diag = [(0, 2), (1, 1), (2, 0)]
        for r, c in diag:
            if rows[r][c] == ' ':
                rows[r][c] = 'O'
                return rows
    #ai attacking move for rows
    for row in rows:
        player, ai = movement_check.checking_row(row)
        idx = movement_check.check_if_movement_is_possible(row)
        if ai == 1 and idx is not False:
            row[idx] = 'O'
            return rows
    #ai check attacking move for columns
    for c in range(3):
        player, ai = movement_check.checking_column(rows, c)
        if ai == 2:
            for r in range(3):
                if rows[r][c] == ' ':
                    rows[r][c] = 'O'
                    return rows
    #ai normal defense moveset
    # ai normal defense move for diagonals
    player, ai = movement_check.checking_diagonal1(rows)
    if player == 1:
        for k in range(3):
            if rows[k][k] == ' ':
                rows[k][k] = 'O'
                return rows

    player, ai = movement_check.checking_diagonal2(rows)
    if player == 1:
        diag = [(0, 2), (1, 1), (2, 0)]
        for r, c in diag:
            if rows[r][c] == ' ':
                rows[r][c] = 'O'
                return rows
    #ai normal defense move for rows
    for row in rows:
        player, ai = movement_check.checking_row(row)
        idx = movement_check.check_if_movement_is_possible(row)
        if player == 1 and idx is not False:
            row[idx] = 'O'
            return rows
    #ai normal defense move for columns
    for c in range(3):
        player, ai = movement_check.checking_column(rows, c)
        if ai == 2:
            for r in range(3):
                if rows[r][c] == ' ':
                    rows[r][c] = 'O'
                    return rows