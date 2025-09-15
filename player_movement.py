def picking_row():
    print('Please select row where you want to pick line: 1, 2 or 3')
    while True:
        u = input().strip()
        if u in ('1', '2', '3'):
            return int(u) - 1
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