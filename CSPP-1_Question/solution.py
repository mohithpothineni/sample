'''Solution for possibilities in sudoku'''



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
            elif collection_rows.count(row_) == 1:
                return 'Invalid Sudoku:Duplicate values'
            else:
                collection_rows.append(row_)
        return ''

def possiblities(sudoku):

    sudoku_bigblocks = []

    for i in range(0,len(sudoku),9):
        sudoku_bigblocks.append(sudoku[i:i+9])

    #print(sudoku_bigblocks)
    for i in sudoku_bigblocks:
        for j in i:
            if (j == '.'):
                possib = []
                for num in range(1,10):
                    if str(num) not in j:
                        possib.append(num)
                    column_ = []
                for col in sudoku_bigblocks:
                    column_.append(col[j])
                for num in range(1,10):
                    if str(num) not in column_:
                        possib.append(num)
                

    #dummy
    return ''

def main():
    sudoku_ = input()
    check_result = check(sudoku_)
    if check_result != '':
        print(check_result)
        return
    for i in possiblities(sudoku_):
        print(i)


if __name__ == "__main__":
    main()

