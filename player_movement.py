import movement_check
def picking_row(rows):
    print('Please select row where you want to pick line: 1, 2 or 3')
    while True:
        u = input().strip()
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
        if u in ('1', '2', '3'):
            col = int(u) - 1
            if row[col] == ' ':
                row[col] = 'X'
                return
            else:
                print('This place is taken.Try to choose another place.')
        else:
            print('Pick from 1, 2 or 3')