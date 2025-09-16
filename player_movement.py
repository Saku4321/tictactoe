import movement_check
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def picking_row(rows):
    print('Please select row where you want to pick line: 1, 2 or 3')
    while True:
        u = input().strip()
        clear_screen()
        if u in ('1', '2', '3'):
            row = int(u)-1
            if movement_check.check_if_movement_is_possible(rows[row]) is False:
                print('These row is full. Try to choose another place.')
            else:
                return row
        print('Select 1, 2 or 3')
def picking_place_in_row(rows, row_idx):
    row = rows[row_idx]
    print('Pick place in row where you want to pick line: 1,2,3')
    while True:
        u = input().strip()
        clear_screen()
        if u in ('1', '2', '3'):
            col = int(u) - 1
            if row[col] == ' ':
                row[col] = 'X'
                return
            else:
                print('This place is taken.Try to choose another place.')
        else:
            print('Pick from 1, 2 or 3')
def picking_place_in_row_for_second_player(rows, row_idx):
    row = rows[row_idx]
    print('Pick place in row where you want to pick line: 1,2,3')
    while True:
        u = input().strip()
        clear_screen()
        if u in ('1', '2', '3'):
            col = int(u) - 1
            if row[col] == ' ':
                row[col] = 'O'
                return
            else:
                print('This place is taken.Try to choose another place.')
        else:
            print('Pick from 1, 2 or 3')

def selecting_game_mode():
    while True:
        print('Select game mode: \n1player\n2player')
        game_mode = input().strip()
        clear_screen()
        if game_mode == '1player':
            return 1
        elif game_mode == '2player':
            return 2
        else:
            print('Wrong game mode. Please try again.')