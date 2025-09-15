import movement_check
def ai_move(rows):
    #ai win-check
        #ai check win move for rows
        for i in rows:
            player, ai = movement_check.checking_row(i)
            if(ai ==2 and movement_check.check_if_movement_is_possible(i)!= False):
                i[movement_check.check_if_movement_is_possible(i)] ='0'
                return rows
        #ai check win move for columns
        for i in range(3):
            player, ai = movement_check.checking_column(rows,i)
            if(ai ==2 and movement_check.check_if_movement_is_possible(i)!= False):
                i[movement_check.check_if_movement_is_possible(i)] ='0'
                return rows
        #ai check win move for diagonals
        player, ai = movement_check.checking_diagonal1(rows)
        if(ai ==2 and movement_check.check_if_movement_is_possible(i)!= False):
            i[movement_check.check_if_movement_is_possible(i)] ='0'
            return rows
        player, ai = movement_check.checking_diagonal2(rows)
        if(ai ==2 and movement_check.check_if_movement_is_possible(i)!= False):
            i[movement_check.check_if_movement_is_possible(i)] ='0'
            return rows
    #ai player-defense
        #ai check defense move for rows
        for i in rows:
            player, ai = movement_check.checking_row(i)
            if(player ==2 and movement_check.check_if_movement_is_possible(i)!= False):
                i[movement_check.check_if_movement_is_possible(i)] ='0'
                return rows
        #ai check defense move for columns
        for i in range(3):
            player, ai = movement_check.checking_column(rows,i)
            if(player ==2 and movement_check.check_if_movement_is_possible(i)!= False):
                i[movement_check.check_if_movement_is_possible(i)] ='0'
                return rows
        #ai check defense move for diagonals
        player, ai = movement_check.checking_diagonal1(rows)
        if(player ==2 and movement_check.check_if_movement_is_possible(i)!= False):
            i[movement_check.check_if_movement_is_possible(i)] ='0'
            return rows
        player, ai = movement_check.checking_diagonal2(rows)
        if(player ==2 and movement_check.check_if_movement_is_possible(i)!= False):
            i[movement_check.check_if_movement_is_possible(i)] ='0'
            return rows
    #ai normal attacking moveset
        #ai attacking move for rows
        for i in rows:
            player, ai = movement_check.checking_row(i)
            if(ai ==1 and movement_check.check_if_movement_is_possible(i)!= False):
                i[movement_check.check_if_movement_is_possible(i)] ='0'
                return rows
        #ai check attacking move for columns
        for i in range(3):
            player, ai = movement_check.checking_column(rows,i)
            if(ai ==1 and movement_check.check_if_movement_is_possible(i)!= False):
                i[movement_check.check_if_movement_is_possible(i)] ='0'
                return rows
        #ai check win move for diagonals
        player, ai = movement_check.checking_diagonal1(rows)
        if(ai ==1 and movement_check.check_if_movement_is_possible(i)!= False):
            i[movement_check.check_if_movement_is_possible(i)] ='0'
            return rows
        player, ai = movement_check.checking_diagonal2(rows)
        if(ai ==1 and movement_check.check_if_movement_is_possible(i)!= False):
            i[movement_check.check_if_movement_is_possible(i)] ='0'
            return rows
    #ai normal defense moveset
        #ai normal defense move for rows
        for i in rows:
            player, ai = movement_check.checking_row(i)
            if(player ==1 and movement_check.check_if_movement_is_possible(i)!= False):
                i[movement_check.check_if_movement_is_possible(i)] ='0'
                return rows
        #ai normal defense move for columns
        for i in range(3):
            player, ai = movement_check.checking_column(rows,i)
            if(player ==1 and movement_check.check_if_movement_is_possible(i)!= False):
                i[movement_check.check_if_movement_is_possible(i)] ='0'
                return rows
        #ai normal defense move for diagonals
        player, ai = movement_check.checking_diagonal1(rows)
        if(player ==1 and movement_check.check_if_movement_is_possible(i)!= False):
            i[movement_check.check_if_movement_is_possible(i)] ='0'
            return rows
        player, ai = movement_check.checking_diagonal2(rows)
        if(player ==1 and movement_check.check_if_movement_is_possible(i)!= False):
            i[movement_check.check_if_movement_is_possible(i)] ='0'
            return rows