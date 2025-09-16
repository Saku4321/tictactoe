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
display(rows)
while True:
    row_idx=player_movement.picking_row()
    player_movement.picking_place_in_row(rows,row_idx)
    display(rows)
    if(movement_check.wincheck(rows)=='True'): break
    ai_movement.ai_move(rows)
    display(rows)
    if(movement_check.wincheck(rows)=='True'): break


