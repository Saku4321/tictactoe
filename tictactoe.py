import player_movement
import movement_check
import ai_movement
def display(rows):
    for i in range(len(rows)):
        print(rows[i])
r1 = [' ',' ',' ']
r2 = [' ',' ',' ']
r3 = [' ',' ',' ']
rows = [r1,r2,r3]
game_mode= player_movement.selecting_game_mode()
if(game_mode==1):
    while True:
        player_movement.clear_screen()
        display(rows)
        row_idx=player_movement.picking_row(rows)
        player_movement.clear_screen()
        display(rows)
        player_movement.picking_place_in_row(rows,row_idx)
        player_movement.clear_screen()
        display(rows)
        if(movement_check.wincheck(rows)==True): break
        ai_movement.ai_move(rows)
        player_movement.clear_screen()
        display(rows)
        if(movement_check.wincheck(rows)==True): break
if(game_mode==2):
    while True:
        player_movement.clear_screen()
        print('X moves')
        display(rows)
        row_idx=player_movement.picking_row(rows)
        player_movement.clear_screen()
        display(rows)
        player_movement.picking_place_in_row(rows,row_idx)
        player_movement.clear_screen()
        display(rows)
        if(movement_check.wincheck(rows)==True): break
        print('O moves')
        row_idx=player_movement.picking_row(rows)
        player_movement.picking_place_in_row_for_second_player(rows,row_idx)
        display(rows)
        if(movement_check.wincheck(rows)==True): break


