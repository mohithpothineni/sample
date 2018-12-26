
def cross(A, B):
    return [a+b for a in A for b in B]



digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits
squares  = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((s, [u for u in unitlist if s in u])
             for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s]))
             for s in squares)




def parse_grid(grid):
    values = dict((s, digits) for s in squares)
    for s,d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False ## (Fail if we can't assign d to square s.)
    return values

def grid_values(grid):
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))

def assign(values, s, d):
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

def eliminate(values, s, d):
    if d not in values[s]:
        return values ## Already eliminated
    values[s] = values[s].replace(d,'')
    if len(values[s]) == 0:
        return False ## Contradiction: removed last value
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
    if len(dplaces) == 0:
        return False ## Contradiction: no place for this value
    elif len(dplaces) == 1:
        if not assign(values, dplaces[0], d):
            return False
    return values

def display(values):
    width = 1+max(len(values[s]) for s in squares)
    for r in rows:
        print(''.join(values[r+c].center(width) for c in cols))


def check(sudoku):
    if (sudoku.count('.') == 0):
        return 'Given sudoku is solved'

    elif(len(sudoku) != 81):
        return 'Invalid input'

    else:
        collection_rows = []
        for i in range(0,len(sudoku),9):
            row_ = [int(j) for j in sudoku[i:i+9] if j != '.']
            set_row = {k for k in row_}
            if len(row_) != len(set_row):
                return 'Invalid Sudoku:Duplicate values'
            elif collection_rows.count(row_) == 1 and len(row_) != 0:
                return 'Invalid Sudoku:Duplicate values'
            else:
                collection_rows.append(row_)
    return ''



def main():
    sudoku = input()
    check_result = check(sudoku)
    if check_result != '':
        print(check_result)
        return
    result_dict = parse_grid(sudoku)    
    #print(result_dict)
    counter = -1
    for key in result_dict.keys():
        counter += 1
        if(sudoku[counter] == '.'):
            print(result_dict[key])

    
if __name__ == '__main__':
    main()

